import dearpygui.dearpygui as dpg
from lib.callback import *
import re

APP_NAME = "BigInt Calculator"
APP_VERSION = "1.0"
app_id = dict()
item_id = "XYZAB"  #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
globe_currenct_base = "16"


def BigInt_base_select(str_in, base):
    match base:
        case "2":
            return re.sub(r"(?<=\w)(?=(?:.{4})+$)", "", str_in)
        case "8":
            return re.sub(r"(?<=\w)(?=(?:.{3})+$)", "", str_in)
        case "10":
            return re.sub(r"(?<=\w)(?=(?:.{3})+$)", "", str_in)
        case "16":
            tmp = re.sub(r"(?<=\w)(?=(?:.{64})+$)", "\n", str_in)
            return re.sub(
                r"(?<=\w)(?=(?:\w{8})+$)", "", tmp.upper(), flags=re.MULTILINE
            )


def BigInt_add(sender, app_data, user_data):
    sel_base = dpg.get_value(user_data["base_radio"])
    s_str_x = "".join(dpg.get_value(user_data["X_input_text"]).replace(",", "").split())
    s_str_y = "".join(dpg.get_value(user_data["Y_input_text"]).replace(",", "").split())
    s_str_z = "".join(dpg.get_value(user_data["Z_input_text"]).replace(",", "").split())
    s_str_a = "".join(dpg.get_value(user_data["A_input_text"]).replace(",", "").split())
    s_str_b = "".join(dpg.get_value(user_data["B_input_text"]).replace(",", "").split())

    if sel_base == "2":
        result = bin(int(s_str_x, int(sel_base)) + int(s_str_y, int(sel_base)))[2:]
        format_str = BigInt_base_select(result, sel_base)
    elif sel_base == "8":
        result = oct(int(s_str_x, int(sel_base)) + int(s_str_y, int(sel_base)))[2:]
        format_str = BigInt_base_select(result, sel_base)
    elif sel_base == "10":
        result = str(int(s_str_x) + int(s_str_y))
        format_str = BigInt_base_select(result, sel_base)
    elif sel_base == "16":
        result = hex(int(s_str_x, int(sel_base)) + int(s_str_y, int(sel_base)))[2:]
        format_str = BigInt_base_select(result, sel_base)

    dpg.set_value(user_data[f"R_input_text"], value=result.upper())
    BigInt_get_bit_length(sender, app_data, user_data)
    # BigInt_result_update(sender, app_data, user_data)


def BigInt_sub(sender, app_data, user_data):
    sel_base = dpg.get_value(user_data["base_radio"])
    s_str_x = "".join(dpg.get_value(user_data["X_input_text"]).replace(",", "").split())
    s_str_y = "".join(dpg.get_value(user_data["Y_input_text"]).replace(",", "").split())
    s_str_z = "".join(dpg.get_value(user_data["Z_input_text"]).replace(",", "").split())
    s_str_a = "".join(dpg.get_value(user_data["A_input_text"]).replace(",", "").split())
    s_str_b = "".join(dpg.get_value(user_data["B_input_text"]).replace(",", "").split())

    match sel_base:
        case "2":
            result = bin(int(s_str_x, int(sel_base)) - int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "8":
            result = oct(int(s_str_x, int(sel_base)) - int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "10":
            result = str(int(s_str_x) - int(s_str_y))
            format_str = BigInt_base_select(result, sel_base)
        case "16":
            result = hex(int(s_str_x, int(sel_base)) - int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)

    dpg.set_value(user_data[f"R_input_text"], value=result.upper())
    BigInt_get_bit_length(sender, app_data, user_data)


def BigInt_mul(sender, app_data, user_data):
    sel_base = dpg.get_value(user_data["base_radio"])
    s_str_x = "".join(dpg.get_value(user_data["X_input_text"]).replace(",", "").split())
    s_str_y = "".join(dpg.get_value(user_data["Y_input_text"]).replace(",", "").split())
    s_str_z = "".join(dpg.get_value(user_data["Z_input_text"]).replace(",", "").split())
    s_str_a = "".join(dpg.get_value(user_data["A_input_text"]).replace(",", "").split())
    s_str_b = "".join(dpg.get_value(user_data["B_input_text"]).replace(",", "").split())

    match sel_base:
        case "2":
            result = bin(int(s_str_x, int(sel_base)) * int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "8":
            result = oct(int(s_str_x, int(sel_base)) * int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "10":
            result = str(int(s_str_x) * int(s_str_y))
            format_str = BigInt_base_select(result, sel_base)
        case "16":
            result = hex(int(s_str_x, int(sel_base)) * int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)

    dpg.set_value(user_data[f"R_input_text"], value=result.upper())
    BigInt_get_bit_length(sender, app_data, user_data)


def BigInt_div(sender, app_data, user_data):
    sel_base = dpg.get_value(user_data["base_radio"])
    s_str_x = "".join(dpg.get_value(user_data["X_input_text"]).replace(",", "").split())
    s_str_y = "".join(dpg.get_value(user_data["Y_input_text"]).replace(",", "").split())
    s_str_z = "".join(dpg.get_value(user_data["Z_input_text"]).replace(",", "").split())
    s_str_a = "".join(dpg.get_value(user_data["A_input_text"]).replace(",", "").split())
    s_str_b = "".join(dpg.get_value(user_data["B_input_text"]).replace(",", "").split())

    match sel_base:
        case "2":
            result = bin(int(s_str_x, int(sel_base)) // int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "8":
            result = oct(int(s_str_x, int(sel_base)) // int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "10":
            result = str(int(s_str_x) // int(s_str_y))
            format_str = BigInt_base_select(result, sel_base)
        case "16":
            result = hex(int(s_str_x, int(sel_base)) // int(s_str_y, int(sel_base)))[2:]
            format_str = BigInt_base_select(result, sel_base)

    dpg.set_value(user_data[f"R_input_text"], value=result.upper())
    BigInt_get_bit_length(sender, app_data, user_data)


def BigInt_x_mul_y_mod_z(sender, app_data, user_data):
    sel_base = dpg.get_value(user_data["base_radio"])
    s_str_x = "".join(dpg.get_value(user_data["X_input_text"]).replace(",", "").split())
    s_str_y = "".join(dpg.get_value(user_data["Y_input_text"]).replace(",", "").split())
    s_str_z = "".join(dpg.get_value(user_data["Z_input_text"]).replace(",", "").split())
    s_str_a = "".join(dpg.get_value(user_data["A_input_text"]).replace(",", "").split())
    s_str_b = "".join(dpg.get_value(user_data["B_input_text"]).replace(",", "").split())

    match sel_base:
        case "2":
            result = bin(
                (int(s_str_x, int(sel_base)) * int(s_str_y, int(sel_base)))
                % int(s_str_z, int(sel_base))
            )[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "8":
            result = oct(
                (int(s_str_x, int(sel_base)) * int(s_str_y, int(sel_base)))
                % int(s_str_z, int(sel_base))
            )[2:]
            format_str = BigInt_base_select(result, sel_base)
        case "10":
            result = str((int(s_str_x) * int(s_str_y)) % int(s_str_z))
            format_str = BigInt_base_select(result, sel_base)
        case "16":
            result = hex(
                (int(s_str_x, int(sel_base)) * int(s_str_y, int(sel_base)))
                % int(s_str_z, int(sel_base))
            )[2:]
            format_str = BigInt_base_select(result, sel_base)

    dpg.set_value(user_data[f"R_input_text"], value=result.upper())
    BigInt_get_bit_length(sender, app_data, user_data)


def BigInt_get_bit_length(sender, app_data, user_data):
    # s = (dpg.get_item_label(sender).split("##")[1])
    for k, v in user_data.items():
        if "_input_text" in k:
            if dpg.get_value(user_data[f"{k[0:-11]}_input_text"]) != "":
                dpg.set_value(
                    user_data[f"{k[0:-11]}_pow"],
                    value=int(
                        dpg.get_value(user_data[f"{k[0:-11]}_input_text"]), 16
                    ).bit_length(),
                )
            else:
                dpg.set_value(user_data[f"{k[0:-11]}_pow"], value="")


def BigInt_send_to_memory(sender, app_data, user_data):
    memory_id = dpg.generate_uuid()
    s = dpg.get_item_label(sender).split("##")[1]
    memory_data_send = dpg.get_value(user_data[f"{s}_input_text"])
    with dpg.table_row(parent=user_data["BigInt_memory_table"]):
        with dpg.group(horizontal=False):
            dpg.add_text(memory_data_send, tag=memory_id, wrap=450)

        with dpg.group(horizontal=False):
            with dpg.group(horizontal=True):
                for i in item_id:
                    if i == "A":
                        break
                    dpg.add_button(
                        label=f"->{i}",
                        tag=f"{i}_{memory_id}",
                        user_data=user_data,
                        callback=BigInt_recall_memory,
                    )
            with dpg.group(horizontal=True):
                for i in item_id:
                    if i == "A" or i == "B":
                        dpg.add_button(
                            label=f"->{i}",
                            tag=f"{i}_{memory_id}",
                            user_data=user_data,
                            callback=BigInt_recall_memory,
                        )
                dpg.add_button(
                    label="X",
                    width=29,
                    user_data=user_data,
                    callback=BigInt_delete_slot_memory,
                )

            with dpg.group():
                dpg.add_input_text(hint="memo", width=103, user_data=user_data)


def BigInt_recall_memory(sender, app_data, user_data):
    # sender_label = dpg.get_item_label(sender)
    for i in item_id:
        if sender[0] == i:
            memory_data = dpg.get_value(int(sender[2:]))
            dpg.set_value(user_data[f"{i}_input_text"], memory_data)
    BigInt_get_bit_length(sender, app_data, user_data)


def BigInt_clear_callback(sender, app_data, user_data):
    s = dpg.get_item_label(sender).split("##")[1]
    batch_set_value(
        [
            user_data[f"{s}_x_input_text"],
            user_data[f"{s}_y_input_text"],
            user_data[f"{s}_neg_y_input_text"],
        ],
        "",
        "",
    )
    get_bit_length(sender, app_data, user_data)


def BigInt_clear_memory(sender, app_data, user_data):
    c = dpg.get_item_info(user_data["BigInt_memory_table"])["children"][1]
    for i in c:
        dpg.delete_item(i)


def BigInt_delete_slot_memory(sender, app_data, user_data):
    for i in range(sender, sender - 11, -1):
        dpg.delete_item(i)


def BigInt_select_type(sender, app_data, user_data):
    global globe_currenct_base
    s_str = dict()
    format_str = dict()
    sel_base = dpg.get_value(sender)
    s = dpg.get_item_label(sender).split("##")[1]

    for i in "XYZABR":
        s_str[i] = "".join(
            dpg.get_value(user_data[f"{i}_input_text"]).replace(",", "").split()
        )
        if s_str[i] != "":
            if globe_currenct_base == "2":
                if sel_base == "2":
                    pass
                elif sel_base == "8":
                    format_str[i] = BigInt_base_select(
                        oct(int(s_str[i], 2))[2:], sel_base
                    )
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "10":
                    format_str[i] = BigInt_base_select(str(int(s_str[i], 2)), sel_base)
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "16":
                    format_str[i] = BigInt_base_select(
                        hex(int(s_str[i], 2))[2:], sel_base
                    )
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])

            elif globe_currenct_base == "8":
                if sel_base == "2":
                    format_str[i] = BigInt_base_select(
                        bin(int(s_str[i], 8))[2:], sel_base
                    )
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "8":
                    pass
                elif sel_base == "10":
                    format_str[i] = BigInt_base_select(str(int(s_str[i], 8)), sel_base)
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "16":
                    format_str[i] = BigInt_base_select(
                        hex(int(s_str[i], 8))[2:], sel_base
                    )
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])

            elif globe_currenct_base == "10":
                if sel_base == "2":
                    format_str[i] = BigInt_base_select(bin(int(s_str[i]))[2:], sel_base)
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "8":
                    format_str[i] = BigInt_base_select(oct(int(s_str[i]))[2:], sel_base)
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "10":
                    pass
                elif sel_base == "16":
                    format_str[i] = BigInt_base_select(hex(int(s_str[i]))[2:], sel_base)
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])

            elif globe_currenct_base == "16":
                if sel_base == "2":
                    format_str[i] = BigInt_base_select(
                        bin(int(s_str[i], 16))[2:], sel_base
                    )
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "8":
                    format_str[i] = BigInt_base_select(
                        oct(int(s_str[i], 16))[2:], sel_base
                    )
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "10":
                    format_str[i] = BigInt_base_select(str(int(s_str[i], 16)), sel_base)
                    dpg.set_value(user_data[f"{i}_input_text"], value=format_str[i])
                elif sel_base == "16":
                    pass
    globe_currenct_base = sel_base


# def BigInt_result_update(sender, app_data, user_data):
#     res_data = dpg.get_value(app_id["R_input_text"])
#     print(res_data)
#     step = (len(res_data)//8)
#     with dpg.table_row(parent=user_data["Result_table"]):
#         for i in range(step):
#             dpg.add_text(res_data[i*8 : i*8+8])
#             dpg.highlight_table_cell(app_id["Result_table"], 0, i, [255, 0, 0, i*255/step])


def BigInt_window():
    dpg.set_viewport_width(1200)
    with dpg.window(
        label=f"{APP_NAME} {APP_VERSION}",
        width=600,
        height=900,
        min_size=[600, 900],
        pos=[600, 0],
        no_resize=False,
        no_close=False,
        on_close=lambda: dpg.set_viewport_width(600),
    ) as app_id[APP_NAME]:
        with dpg.child_window(width=-1, height=90 * len(item_id)):
            for i in item_id:
                with dpg.group(label=f"group_{i}##{APP_NAME}"):
                    with dpg.group(horizontal=True):
                        with dpg.table(
                            label=f"table_{i}##{APP_NAME}",
                            header_row=False,
                            borders_innerH=False,
                            borders_innerV=False,
                            borders_outerH=False,
                        ) as app_id[f"table_{i}"]:
                            dpg.add_table_column(width=10, width_fixed=True)
                            dpg.add_table_column(
                                width_stretch=True, init_width_or_weight=0.0
                            )
                            dpg.add_table_column(width_fixed=True)
                            dpg.add_table_column(width_fixed=True)

                            with dpg.table_row():
                                # group name
                                dpg.add_text(f"{i}", color=[255, 0, 0])

                                # pow
                                app_id[f"{i}_pow"] = dpg.add_text(
                                    label=f"##pow##{i}##{APP_NAME}"
                                )
                                with dpg.group(horizontal=True):
                                    # base point
                                    # app_id[f"{i}_base_button"] = dpg.add_button(
                                    #     label=f"basePoint##{i}##{APP_NAME}",
                                    #     user_data=app_id,
                                    #     callback=lambda s, a, u: dpg.set_value(u[f"{(dpg.get_item_label(s).split('##')[1])}_input_text"], value=hex(ORDER)[2:].zfill(64).upper())
                                    # )
                                    app_id[f"{i}_n_button"] = dpg.add_button(
                                        label=f"n##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=lambda s, a, u: dpg.set_value(
                                            u[
                                                f"{(dpg.get_item_label(s).split('##')[1])}_input_text"
                                            ],
                                            value=hex(ORDER)[2:].zfill(64).upper(),
                                        ),
                                    )
                                    app_id[f"{i}_p_button"] = dpg.add_button(
                                        label=f"p##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=lambda s, a, u: dpg.set_value(
                                            u[
                                                f"{(dpg.get_item_label(s).split('##')[1])}_input_text"
                                            ],
                                            value=hex(p)[2:].zfill(64).upper(),
                                        ),
                                    )
                                    app_id[f"{i}_beta_button"] = dpg.add_button(
                                        label=f"beta##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=lambda s, a, u: dpg.set_value(
                                            u[
                                                f"{(dpg.get_item_label(s).split('##')[1])}_input_text"
                                            ],
                                            value=hex(BETA)[2:].zfill(64).upper(),
                                        ),
                                    )
                                    app_id[f"{i}_lambda_button"] = dpg.add_button(
                                        label=f"lambda##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=lambda s, a, u: dpg.set_value(
                                            u[
                                                f"{(dpg.get_item_label(s).split('##')[1])}_input_text"
                                            ],
                                            value=hex(LAMBDA)[2:].zfill(64).upper(),
                                        ),
                                    )

                                with dpg.group(horizontal=True):
                                    # Memory
                                    app_id[f"{i}_to_memory_button"] = dpg.add_button(
                                        label=f"->Memory##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=BigInt_send_to_memory,
                                    )
                                    # Clear
                                    app_id[f"{i}_clear_button"] = dpg.add_button(
                                        label=f"Clear##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=lambda s, a, u: dpg.set_value(
                                            u[
                                                f"{(dpg.get_item_label(s).split('##')[1])}_input_text"
                                            ],
                                            value="",
                                        ),
                                    )

                    # input text group
                    with dpg.group(
                        label=f"group_{i}##{APP_NAME}", horizontal=True
                    ) as app_id[f"group_{i}"]:
                        input_text = ""
                        app_id[f"{i}_input_text"] = dpg.add_input_text(
                            label=f"##{i}##{APP_NAME}",
                            multiline=True,
                            width=-1,
                            height=55,
                            uppercase=True,
                            default_value=input_text,
                            user_data=app_id,
                            callback=BigInt_get_bit_length,
                        )

        # Result group
        with dpg.child_window(width=-1, height=110):
            with dpg.group(label=f"group_result##{APP_NAME}"):
                with dpg.table(
                    label=f"table_{i}##{APP_NAME}",
                    header_row=False,
                    borders_innerH=False,
                    borders_outerH=False,
                    borders_innerV=False,
                ) as app_id[f"table_{i}"]:
                    dpg.add_table_column(width=10, width_fixed=True)
                    dpg.add_table_column(width_stretch=True, init_width_or_weight=0.0)
                    dpg.add_table_column(width_fixed=True)

                    with dpg.table_row():
                        dpg.add_text("Result", color=[255, 0, 0])
                        # pow
                        app_id[f"R_pow"] = dpg.add_text(label=f"##pow##R##{APP_NAME}")
                        with dpg.group(horizontal=True):
                            app_id["R_to_clipbaord_button"] = dpg.add_button(
                                label=f"->C##R##{APP_NAME}",
                                user_data=app_id,
                                callback=lambda s, a, u: dpg.set_clipboard_text(
                                    dpg.get_value(u["R_input_text"])
                                ),
                            )
                            with dpg.tooltip(dpg.last_item()):
                                dpg.add_text("send value to clipboard")

                            app_id["R_to_memory_button"] = dpg.add_button(
                                label=f"->Memory##R##{APP_NAME}",
                                user_data=app_id,
                                callback=BigInt_send_to_memory,
                            )
                            app_id["R_clear_button"] = dpg.add_button(
                                label=f"Clear##R##{APP_NAME}",
                                user_data=app_id,
                                callback=lambda s, a, u: dpg.set_value(
                                    u[
                                        f"{(dpg.get_item_label(s).split('##')[1])}_input_text"
                                    ],
                                    value="",
                                ),
                            )

                # with dpg.table(
                #     # label=f"Result_table##{APP_NAME}",
                #     header_row=False,
                #     borders_innerH=True,
                #     borders_outerH=True,
                #     borders_innerV=True,
                #     borders_outerV=True,
                #     row_background=True,
                # ) as app_id["Result_table"]:
                #     for i in range(8):
                #         dpg.add_table_column()

                app_id["R_input_text"] = dpg.add_text(wrap=450)
                # with dpg.table_row():
                #     for i in range(8,0,-1):
                #         app_id["R_input_text"] = dpg.add_text()
                #         dpg.highlight_table_cell(app_id["Result_table"], 0, i, [255, 0, 0, i*255/8])
                # with dpg.group(horizontal=True):
                #     app_id["R_input_text"] = dpg.add_text(
                #         label=f"##Z##{APP_NAME}",
                #         # multiline=True,
                #         wrap=450,
                #         # width=-1,
                #         # height=60,
                #         # hexadecimal=True,
                #         # uppercase=True,
                #         user_data=app_id,
                #         # callback=BigInt_get_bit_length,
                #     )

        # Base group
        with dpg.child_window(width=-1, height=35):
            with dpg.group(horizontal=True):
                dpg.add_text("Base", color=[255, 0, 0])
                app_id["base_radio"] = dpg.add_radio_button(
                    label=f"base##{APP_NAME}",
                    items=("2", "8", "10", "16", "64", "256"),
                    default_value="16",
                    horizontal=True,
                    user_data=app_id,
                    callback=BigInt_select_type,
                )

        # operation
        with dpg.child_window(width=-1, height=35):
            with dpg.group(horizontal=True):
                dpg.add_text("Operation", color=[255, 0, 0])
                dpg.add_button(
                    label=f"X + Y##{APP_NAME}", user_data=app_id, callback=BigInt_add
                )
                dpg.add_button(
                    label=f"X - Y##{APP_NAME}", user_data=app_id, callback=BigInt_sub
                )
                dpg.add_button(
                    label=f"X * Y##{APP_NAME}", user_data=app_id, callback=BigInt_mul
                )
                dpg.add_button(
                    label=f"X / Y##{APP_NAME}", user_data=app_id, callback=BigInt_div
                )
                dpg.add_button(
                    label=f"X * Y Mod Z##{APP_NAME}",
                    user_data=app_id,
                    callback=BigInt_x_mul_y_mod_z,
                )

        # cmd group
        with dpg.child_window(width=-1, height=62):
            with dpg.group(label=f"group_cmd##{APP_NAME}"):
                with dpg.group(horizontal=True):
                    with dpg.table(
                        header_row=False,
                        borders_innerH=False,
                        borders_outerH=False,
                        borders_innerV=False,
                    ):
                        dpg.add_table_column(
                            width_stretch=True, init_width_or_weight=0.0
                        )
                        dpg.add_table_column(width_fixed=True)

                        with dpg.table_row():
                            dpg.add_text("Command", color=[255, 0, 0])
                            # dpg.add_spacer(width=506)
                            app_id["cmd_clear_button"] = dpg.add_button(
                                label=f"Clear##cmd##{APP_NAME}",
                                user_data=app_id,
                                callback=lambda s, a, u: dpg.set_value(
                                    u[
                                        f"{(dpg.get_item_label(s).split('##')[1])}_input"
                                    ],
                                    value="",
                                ),
                            )

                with dpg.group(horizontal=True):
                    app_id["cmd_input"] = dpg.add_input_text(
                        label=f"##cmd##{APP_NAME}",
                        # multiline=True,
                        width=-1,
                        # height=45,
                        uppercase=True,
                        on_enter=True,
                        user_data=app_id,
                    )

        # Memory
        with dpg.child_window(autosize_x=True, autosize_y=True, no_scrollbar=True):
            with dpg.table(
                header_row=False,
                borders_innerH=False,
                borders_outerH=False,
                borders_innerV=False,
            ) as app_id[f"table_memory"]:
                # dpg.add_table_column(width_fixed=True)
                dpg.add_table_column(width_stretch=True, init_width_or_weight=0.0)
                dpg.add_table_column(width_fixed=True)

                with dpg.table_row():
                    dpg.add_table_cell()
                    dpg.add_button(
                        label=f"Clear All##{APP_NAME}",
                        user_data=app_id,
                        callback=BigInt_clear_memory,
                    )

            with dpg.table(
                header_row=True,
                policy=dpg.mvTable_SizingFixedFit,
                row_background=True,
                resizable=False,
                no_host_extendX=False,
                hideable=True,
                delay_search=True,
                borders_innerV=True,
                borders_outerV=True,
                borders_innerH=True,
                borders_outerH=True,
                # tag="BigInt_memory_table"
            ) as app_id["BigInt_memory_table"]:
                dpg.add_table_column(
                    label="Memory", width_stretch=True, init_width_or_weight=0.0
                )

                dpg.add_table_column(label="Operation", width=10, width_fixed=True)

