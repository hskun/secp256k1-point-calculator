import dearpygui.dearpygui as dpg
# from dearpygui_ext.logger import mvLogger
import lib.ecdsa as BitcoinEcdsa

dpg.create_context()

# logger = mvLogger()
# dpg.configure_item(21, pos=(0,620), width=600, height=300)
ecdsa = BitcoinEcdsa.Ecdsa()
ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
BETA = 0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee
LAMBDA = 0x5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72

def batch_set_value(sender, app_data, user_data):
    for item in sender:
        dpg.set_value(item, value=user_data)


def get_bit_length(sender, app_data, user_data):
    # s = (dpg.get_item_label(sender).split("##")[1])
    for k, v in user_data.items():
        if "_input_text" in k:
            if dpg.get_value(user_data[f"{k[0:-11]}_input_text"]) != "":
                dpg.set_value(user_data[f"{k[0:-11]}_pow"], value=int(
                    dpg.get_value(user_data[f"{k[0:-11]}_input_text"]), 16).bit_length())
            else:
                dpg.set_value(user_data[f"{k[0:-11]}_pow"], value='')

def log_warning(sender, app_data, user_data):
    dpg.configure_item(user_data["log_text"], color=[255, 0, 0])
    dpg.set_value(user_data["log_text"], value=f"Warning: {app_data}")


def add_one_callback(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    s_str = dpg.get_value(user_data[f"{s}_input_text"])
    try:
        # dpg.configure_item(user_data[f"group_public_key"], show=True)
        result = 1 if s_str=='' else (int(s_str, 16) + 1)
        dpg.set_value(user_data[f"{s}_input_text"],
                    value=hex(result)[2:].zfill(64).upper())
        calculate_public_key(result, user_data)
    except (RuntimeError, TypeError, NameError) as e:
        print(e)
    get_bit_length(sender, app_data, user_data)

def sub_one_callback(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    s_str = dpg.get_value(user_data[f"{s}_input_text"])
    try:
        result = 0 if s_str=='' else (int(s_str, 16) - 1)
        if result > 0:
            dpg.set_value(user_data[f"{s}_input_text"],
                        value=hex(result)[2:].zfill(64).upper())
            calculate_public_key(result, user_data)
        else:
            pass
    except (RuntimeError, TypeError, NameError):
        print("get error")
    get_bit_length(sender, app_data, user_data)

def drag_pow_callback(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    dpg.set_value(user_data[f"{s}_x_input_text"],
                  value=hex(2 ** dpg.get_value(sender))[2:])


def base_point_callback(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    _, public_key = ecdsa.make_keypair(1)
    _, neg_y = (ecdsa.point_neg(public_key))
    dpg.set_value(user_data[f"{s}_x_input_text"],
                  value=hex(public_key[0])[2:].zfill(64).upper())
    dpg.set_value(user_data[f"{s}_y_input_text"],
                  value=hex(public_key[1])[2:].zfill(64).upper())
    dpg.set_value(user_data[f"{s}_neg_y_input_text"],
                  value=hex(neg_y)[2:].zfill(64).upper())


def get_y_coordinate(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    try:
        x = int(dpg.get_value(user_data[f"{s}_x_input_text"]), 16)
        y, neg_y = ecdsa.get_y_coordinate(x)
        if ecdsa.is_on_curve((x, y)):
            dpg.set_value(user_data[f"{s}_y_input_text"],
                        value=hex(y)[2:].zfill(64).upper())
            dpg.set_value(user_data[f"{s}_neg_y_input_text"],
                        value=hex(neg_y)[2:].zfill(64).upper())
        else:
            log_warning(None, "No Point(x,y) on the curve for this x-coordinate.", user_data)
            pass
    except (RuntimeError, TypeError, NameError):
        print("get error")
    get_bit_length(sender, app_data, user_data)

def send_to_memory(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    x_value = dpg.get_value(user_data[f"{s}_x_input_text"])
    y_value = dpg.get_value(user_data[f"{s}_y_input_text"])
    with dpg.table_row(parent=user_data["memory"]):
        with dpg.group(horizontal=False):
            dpg.add_text(x_value)
            dpg.add_text(y_value)

        with dpg.group(horizontal=False):
            with dpg.group(horizontal=True):
                dpg.add_button(label="->A", user_data=user_data,
                            callback=recall_memory)
                dpg.add_button(label="->B", user_data=user_data,
                            callback=recall_memory)
                dpg.add_button(label="X", width=26,
                            user_data=user_data, callback=delete_slot_memory)
            
            with dpg.group(horizontal=False):
                dpg.add_input_text(hint="memo", width=100, user_data=user_data)


def clear_callback(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    batch_set_value([user_data[f"{s}_x_input_text"], user_data[f"{s}_y_input_text"],
                    user_data[f"{s}_neg_y_input_text"]], "", "")
    get_bit_length(sender, app_data, user_data)


def recall_memory(sender, app_data, user_data):
    sander_label = dpg.get_item_label(sender)
    if sander_label[2] == "A":
        # s = (dpg.get_item_label(sender).split("##")[1])
        mem_x = dpg.get_value(sender-4)
        mem_y = dpg.get_value(sender-3)
        if dpg.get_value(user_data[f"{sander_label[2]}_radio_button"]) == "Vector":
            dpg.set_value(user_data["A_x_input_text"], mem_x)
            dpg.set_value(user_data["A_y_input_text"], mem_y)
        else:
            dpg.set_value(user_data["A_x_input_text"], mem_x)
        dpg.set_value(user_data["A_neg_y_input_text"], "")
    else:
        mem_x = dpg.get_value(sender-5)
        mem_y = dpg.get_value(sender-4)
        if dpg.get_value(user_data[f"{sander_label[2]}_radio_button"]) == "Vector":
            dpg.set_value(user_data["B_x_input_text"], mem_x)
            dpg.set_value(user_data["B_y_input_text"], mem_y)
        else:
            dpg.set_value(user_data["B_x_input_text"], mem_x)
        dpg.set_value(user_data["B_neg_y_input_text"], "")
    get_bit_length(sender, app_data, user_data)


def delete_slot_memory(sender, app_data, user_data):
    for i in range(sender, sender-9, -1):
        dpg.delete_item(i)


def clear_memory(sender, app_data, user_data):
    c = dpg.get_item_info(user_data["memory"])["children"][1]
    for i in c:
        dpg.delete_item(i)


def calculate_public_key(result, user_data):
    _, public_key = ecdsa.make_keypair(result)
    _, neg_y = (ecdsa.point_neg(public_key))
    dpg.set_value(user_data["public_x_input_text"],
                  value=hex(public_key[0])[2:].zfill(64).upper())
    dpg.set_value(user_data["public_y_input_text"],
                  value=hex(public_key[1])[2:].zfill(64).upper())
    dpg.set_value(user_data["public_neg_y_input_text"],
                  value=hex(neg_y)[2:].zfill(64).upper())
    get_bit_length(None, None, user_data)


def select_type(sender, app_data, user_data):
    sel_type = dpg.get_value(sender)
    s = (dpg.get_item_label(sender).split("##")[1])
    toggle_items = [user_data[f"{s}_base_point_button"], user_data[f"{s}_y_neg_y_button"],
                    user_data[f"{s}_y_input_text"], user_data[f"{s}_neg_y_input_text"]]
    if sel_type == "Vector":  # vector
        dpg.configure_item(user_data[f"{s}_drag_int"], enabled=False)
        dpg.configure_item(user_data[f"table_{s}_y"], show=True)
        dpg.configure_item(user_data[f"table_{s}_neg_y"], show=True)
        for item in toggle_items:
            dpg.configure_item(item, enabled=True)
    if sel_type == "Scalar":  # scalar
        dpg.configure_item(user_data[f"{s}_drag_int"], enabled=True)
        dpg.configure_item(user_data[f"table_{s}_y"], show=False)
        dpg.configure_item(user_data[f"table_{s}_neg_y"], show=False)
        for item in toggle_items:
            dpg.configure_item(item, enabled=False)
    # batch_set_value([user_data[f"{s}_x_input_text"], user_data[f"{s}_y_input_text"], user_data[f"{s}_neg_y_input_text"]], "", "")


def rand_callback(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    private_key, public_key = ecdsa.make_keypair()
    Q = ecdsa.public_key(public_key)
    _, neg_y = (ecdsa.point_neg(public_key))
    uncompressed_address = ecdsa.public_key_to_address(Q)
    ripemd160 = ecdsa.public_key_to_ripemd160(Q)
    if dpg.get_value(user_data[f"{s}_radio_button"]) == "Vector":  # vector
        dpg.set_value(user_data[f"{s}_x_input_text"],
                      value=hex(public_key[0])[2:].zfill(64).upper())
        dpg.set_value(user_data[f"{s}_y_input_text"],
                      value=hex(public_key[1])[2:].zfill(64).upper())
        dpg.set_value(user_data[f"{s}_neg_y_input_text"],
                      value=hex(neg_y)[2:].zfill(64).upper())
    else:  # scalar
        dpg.set_value(user_data[f"{s}_x_input_text"],
                      value=hex(private_key)[2:].zfill(64).upper())
        batch_set_value(
            [user_data[f"{s}_y_input_text"], user_data[f"{s}_neg_y_input_text"]], "", "")
    get_bit_length(sender, app_data, user_data)


def transposition_callback(sender, app_data, user_data):
    s = (dpg.get_item_label(sender).split("##")[1])
    if dpg.get_value(user_data[f"{s}_radio_button"]) == "Vector":  # vector
        _y = dpg.get_value(user_data[f"{s}_y_input_text"])
        neg_y = dpg.get_value(user_data[f"{s}_neg_y_input_text"])
        _y, neg_y = neg_y, _y
        dpg.set_value(user_data[f"{s}_y_input_text"], value=_y)
        dpg.set_value(user_data[f"{s}_neg_y_input_text"], value=neg_y)
    get_bit_length(sender, app_data, user_data)


def add_callback(sender, app_data, user_data):
    sel_type_a = dpg.get_value(user_data["A_radio_button"])
    sel_type_b = dpg.get_value(user_data["B_radio_button"])

    if sel_type_a == "Scalar" and sel_type_b == "Scalar":  # a scalar, b scalar
        A_x = dpg.get_value(user_data["A_x_input_text"])
        B_x = dpg.get_value(user_data["B_x_input_text"])
        if A_x != "" and B_x != "":
            result = (int(A_x, 16) + int(B_x, 16)) % int(ORDER)
            dpg.set_value(user_data["C_x_input_text"],
                          value=hex(result)[2:].zfill(64).upper())
            dpg.configure_item(user_data["C_y_input_text"], enabled=False)
            dpg.configure_item(user_data["C_neg_y_input_text"], enabled=False)
            batch_set_value([user_data["C_y_input_text"],
                            user_data["C_neg_y_input_text"]], "", "")

            _, public_key = ecdsa.make_keypair(result)
            _, neg_y = (ecdsa.point_neg(public_key))
            dpg.set_value(user_data["public_x_input_text"],
                          value=hex(public_key[0])[2:].zfill(64).upper())
            dpg.set_value(user_data["public_y_input_text"],
                          value=hex(public_key[1])[2:].zfill(64).upper())
            dpg.set_value(user_data["public_neg_y_input_text"], value=hex(
                neg_y)[2:].zfill(64).upper())
        else:
            log_warning(None, "error.", user_data)
            pass

    elif sel_type_a == "Vector" and sel_type_b == "Vector":  # a vector, b vector
        A_x = dpg.get_value(user_data["A_x_input_text"])
        A_y = dpg.get_value(user_data["A_y_input_text"])
        B_x = dpg.get_value(user_data["B_x_input_text"])
        B_y = dpg.get_value(user_data["B_y_input_text"])
        if A_x != "" and A_y != "" and B_x != "" and B_y != "":
            dpg.configure_item(user_data["C_y_input_text"], enabled=True)
            dpg.configure_item(user_data["C_neg_y_input_text"], enabled=True)
            batch_set_value([user_data["public_x_input_text"], user_data["public_y_input_text"],
                            user_data["public_neg_y_input_text"]], "", "")
            point_a = (int(A_x, 16), int(A_y, 16))
            point_b = (int(B_x, 16), int(B_y, 16))
            if ecdsa.is_on_curve(point_a) == False or ecdsa.is_on_curve(point_b) == False:
                log_warning(None, "point is not on curve.", user_data)
                pass
            else:
                result = ecdsa.point_add(point_a, point_b)
                if result == None:
                    batch_set_value(
                        [user_data["C_x_input_text"], user_data["C_y_input_text"], user_data["C_neg_y_input_text"]], "", 0)
                else:
                    _, neg_y = ecdsa.point_neg(result)
                    dpg.set_value(user_data["C_x_input_text"], value=hex(
                        result[0])[2:].zfill(64).upper())
                    dpg.set_value(user_data["C_y_input_text"], value=hex(
                        result[1])[2:].zfill(64).upper())
                    dpg.set_value(user_data["C_neg_y_input_text"], value=hex(
                        neg_y)[2:].zfill(64).upper())
        else:
            log_warning(None, "please input point A, B value.", user_data)
            pass
    else:
        batch_set_value([user_data["C_x_input_text"], user_data["C_y_input_text"],
                        user_data["C_neg_y_input_text"]], "", "")
        log_warning(None, "not support operation.", user_data)
        pass
    get_bit_length(sender, app_data, user_data)


def sub_callback(sender, app_data, user_data):
    sel_type_a = dpg.get_value(user_data["A_radio_button"])
    sel_type_b = dpg.get_value(user_data["B_radio_button"])
    if sel_type_a == "Scalar" and sel_type_b == "Scalar":  # a scalar, b scalar
        A_x = dpg.get_value(user_data["A_x_input_text"])
        B_x = dpg.get_value(user_data["B_x_input_text"])
        if A_x != "" and B_x != "":
            result = (int(A_x, 16) - int(B_x, 16)) % int(ORDER)
            dpg.set_value(user_data["C_x_input_text"],
                          value=hex(result)[2:].zfill(64).upper())
            dpg.configure_item(user_data["C_y_input_text"], enabled=False)
            dpg.configure_item(user_data["C_neg_y_input_text"], enabled=False)
            batch_set_value([user_data["C_y_input_text"],
                            user_data["C_neg_y_input_text"]], "", "")

            _, public_key = ecdsa.make_keypair(result)
            _, neg_y = ecdsa.point_neg(public_key)
            dpg.set_value(user_data["public_x_input_text"],
                          value=hex(public_key[0])[2:].zfill(64).upper())
            dpg.set_value(user_data["public_y_input_text"],
                          value=hex(public_key[1])[2:].zfill(64).upper())
            dpg.set_value(user_data["public_neg_y_input_text"], value=hex(
                neg_y)[2:].zfill(64).upper())
        else:
            # logger.log_warning("error.")
            pass
    elif sel_type_a == "Vector" and sel_type_b == "Vector":  # a vector, b vector
        A_x = dpg.get_value(user_data["A_x_input_text"])
        A_y = dpg.get_value(user_data["A_y_input_text"])
        B_x = dpg.get_value(user_data["B_x_input_text"])
        B_y = dpg.get_value(user_data["B_y_input_text"])
        if A_x != "" and A_y != "" and B_x != "" and B_y != "":
            dpg.configure_item(user_data["C_y_input_text"], enabled=True)
            dpg.configure_item(user_data["C_neg_y_input_text"], enabled=True)
            batch_set_value([user_data["public_x_input_text"], user_data["public_y_input_text"],
                            user_data["public_neg_y_input_text"]], "", "")
            point_a = (int(A_x, 16), int(A_y, 16))
            point_b = (int(B_x, 16), int(B_y, 16))
            if ecdsa.is_on_curve(point_a) == False or ecdsa.is_on_curve(point_b) == False:
                log_warning(None, "point is not on curve.", user_data)
                pass
            else:
                result = ecdsa.point_sub(point_a, point_b)
                if result == None:
                    batch_set_value(
                        [user_data["C_x_input_text"], user_data["C_y_input_text"], user_data["C_neg_y_input_text"]], "", 0)
                else:
                    _, neg_y = ecdsa.point_neg(result)
                    dpg.set_value(user_data["C_x_input_text"], value=hex(
                        result[0])[2:].zfill(64).upper())
                    dpg.set_value(user_data["C_y_input_text"], value=hex(
                        result[1])[2:].zfill(64).upper())
                    dpg.set_value(user_data["C_neg_y_input_text"], value=hex(
                        neg_y)[2:].zfill(64).upper())
        else:
            log_warning(None, "please input point A, B value.", user_data)
            pass
    else:
        batch_set_value([user_data["C_x_input_text"], user_data["C_y_input_text"],
                        user_data["C_neg_y_input_text"]], "", "")
        log_warning(None, "not support operation.", user_data)
        pass
    get_bit_length(sender, app_data, user_data)


def mul_callback(sender, app_data, user_data):
    sel_type_a = dpg.get_value(user_data["A_radio_button"])
    sel_type_b = dpg.get_value(user_data["B_radio_button"])
    if (sel_type_a == "Scalar" and sel_type_b == "Scalar"):  # a scalar, b scalar
        A_x = dpg.get_value(user_data["A_x_input_text"])
        B_x = dpg.get_value(user_data["B_x_input_text"])
        if A_x != "" and B_x != "":
            result = (int(A_x, 16) * int(B_x, 16)) % int(ORDER)
            dpg.set_value(user_data["C_x_input_text"],
                          value=hex(result)[2:].zfill(64).upper())
            dpg.configure_item(user_data["C_y_input_text"], enabled=False)
            dpg.configure_item(user_data["C_neg_y_input_text"], enabled=False)
            batch_set_value([user_data["C_y_input_text"],
                            user_data["C_neg_y_input_text"]], "", "")

            _, public_key = ecdsa.make_keypair(result)
            _, neg_y = (ecdsa.point_neg(public_key))
            dpg.set_value(user_data["public_x_input_text"],
                          value=hex(public_key[0])[2:].zfill(64).upper())
            dpg.set_value(user_data["public_y_input_text"],
                          value=hex(public_key[1])[2:].zfill(64).upper())
            dpg.set_value(user_data["public_neg_y_input_text"], value=hex(
                neg_y)[2:].zfill(64).upper())
        else:
            # logger.log_warning("error.")
            pass
    elif sel_type_a == "Vector" and sel_type_b == "Vector":  # a vector, b vector
        batch_set_value([user_data["C_x_input_text"], user_data["C_y_input_text"],
                        user_data["C_neg_y_input_text"]], "", "")
        log_warning(None, "not support operation.", user_data)
        pass
    elif sel_type_a == "Scalar" and sel_type_b == "Vector":  # a scalar, b vector:
        A_x = dpg.get_value(user_data["A_x_input_text"])
        B_x = dpg.get_value(user_data["B_x_input_text"])
        B_y = dpg.get_value(user_data["B_y_input_text"])
        point_b = (int(B_x, 16), int(B_y, 16))
        if ecdsa.is_on_curve(point_b) == False:
            log_warning(None, "point B is not on curve.", user_data)
            pass
        elif A_x != "" and B_x != "" and B_y != "":
            result = ecdsa.scalar_multiply(
                int(A_x, 16), (int(B_x, 16), int(B_y, 16)), 0)
            _, neg_y = (ecdsa.point_neg(result))
            dpg.configure_item(user_data["C_y_input_text"], enabled=True)
            dpg.configure_item(user_data["C_neg_y_input_text"], enabled=True)
            batch_set_value([user_data["public_x_input_text"], user_data["public_y_input_text"],
                            user_data["public_neg_y_input_text"]], "", "")
            dpg.set_value(user_data["C_x_input_text"],
                          value=hex(result[0])[2:].zfill(64).upper())
            dpg.set_value(user_data["C_y_input_text"],
                          value=hex(result[1])[2:].zfill(64).upper())
            dpg.set_value(user_data["C_neg_y_input_text"],
                          value=hex(neg_y)[2:].zfill(64).upper())
    elif sel_type_a == "Vector" and sel_type_b == "Scalar":  # a vector, b scalar:
        A_x = dpg.get_value(user_data["A_x_input_text"])
        A_y = dpg.get_value(user_data["A_y_input_text"])
        B_x = dpg.get_value(user_data["B_x_input_text"])
        point_a = (int(A_x, 16), int(A_y, 16))
        if ecdsa.is_on_curve(point_a) == False:
            log_warning(None, "point A is not on curve.", user_data)
            pass
        elif A_x != "" and A_y != "" and B_x != "":
            result = ecdsa.scalar_multiply(
                int(B_x, 16), (int(A_x, 16), int(A_y, 16)), 0)
            _, neg_y = (ecdsa.point_neg(result))
            dpg.configure_item(user_data["C_y_input_text"], enabled=True)
            dpg.configure_item(user_data["C_neg_y_input_text"], enabled=True)
            batch_set_value([user_data["public_x_input_text"], user_data["public_y_input_text"],
                            user_data["public_neg_y_input_text"]], "", "")
            dpg.set_value(user_data["C_x_input_text"],
                          value=hex(result[0])[2:].zfill(64).upper())
            dpg.set_value(user_data["C_y_input_text"],
                          value=hex(result[1])[2:].zfill(64).upper())
            dpg.set_value(user_data["C_neg_y_input_text"],
                          value=hex(neg_y)[2:].zfill(64).upper())
        else:
            log_warning(None, "error.", user_data)
            pass
    get_bit_length(sender, app_data, user_data)

def div_callback(sender, app_data, user_data):
    get_bit_length(sender, app_data, user_data)


# dpg.create_viewport()
dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
dpg.destroy_context()
