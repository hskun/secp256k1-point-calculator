import dearpygui.dearpygui as dpg
from lib.callback import *

dpg.create_context()

APP_NAME = "secp256k1 point Calculator"
APP_VERSION = "1.3"
app_id = dict()


def add_app_window():
    with dpg.window(
        label=APP_NAME,
        width=600,
        height=550,
        pos=[0, 0],
        no_resize=True,
        no_move=True,
        no_close=True,
        no_collapse=True,
        no_title_bar=True,
    ) as app_id[APP_NAME]:
        with dpg.menu_bar():
            with dpg.menu(label="Help"):
                dpg.add_menu_item(
                    label="Show About", callback=lambda: dpg.show_tool(dpg.mvTool_About)
                )

                dpg.add_menu_item(
                    label="Show Metrics",
                    callback=lambda: dpg.show_tool(dpg.mvTool_Metrics),
                )

                dpg.add_menu_item(
                    label="Show Documentation",
                    callback=lambda: dpg.show_tool(dpg.mvTool_Doc),
                )

                dpg.add_menu_item(
                    label="Show Debug", callback=lambda: dpg.show_tool(dpg.mvTool_Debug)
                )

                dpg.add_menu_item(
                    label="Show Style Editor",
                    callback=lambda: dpg.show_tool(dpg.mvTool_Style),
                )

                dpg.add_menu_item(
                    label="Show Font Manager",
                    callback=lambda: dpg.show_tool(dpg.mvTool_Font),
                )

                dpg.add_menu_item(
                    label="Show Item Registry",
                    callback=lambda: dpg.show_tool(dpg.mvTool_ItemRegistry),
                )

                dpg.add_menu_item(
                    label="Show ImGui Demo", callback=lambda: dpg.show_imgui_demo()
                )

                dpg.add_menu_item(
                    label="Show ImPlot Demo", callback=lambda: dpg.show_implot_demo()
                )

        for i in "AB":
            with dpg.child_window(width=-1, height=110):
                with dpg.group(label=f"group_{i}##{APP_NAME}"):
                    with dpg.group(horizontal=True):
                        dpg.add_text(f" {i}", color=[255, 0, 0])

                        app_id[f"{i}_radio_button"] = dpg.add_radio_button(
                            label=f"radio##{i}##{APP_NAME}",
                            items=("Vector", "Scalar"),
                            default_value="Vector",
                            horizontal=True,
                            user_data=app_id,
                            callback=select_type,
                        )

                        app_id[f"{i}_rand_button"] = dpg.add_button(
                            label=f"RAND##{i}##{APP_NAME}",
                            user_data=app_id,
                            callback=rand_callback,
                        )

                        app_id[f"{i}_g_point_button"] = dpg.add_button(
                            label=f"G Point##{i}##{APP_NAME}",
                            user_data=app_id,
                            callback=g_point_callback,
                        )

                        dpg.add_text("2^")

                        app_id[f"{i}_drag_int"] = dpg.add_drag_int(
                            label=f"##{i}##{APP_NAME}",
                            min_value=0,
                            max_value=256,
                            width=75,
                            user_data=app_id,
                            callback=drag_pow_callback,
                        )

                        app_id[f"{i}_to_memory_button"] = dpg.add_button(
                            label=f"->Memory##{i}##{APP_NAME}",
                            indent=448,
                            user_data=app_id,
                            callback=send_to_memory,
                        )

                        app_id[f"{i}_clear_button"] = dpg.add_button(
                            label=f"Clear##{i}##{APP_NAME}",
                            user_data=app_id,
                            callback=clear_callback,
                        )

                    with dpg.group(
                        label=f"group_x_{i}##{APP_NAME}", horizontal=True
                    ) as app_id[f"group_x_{i}"]:
                        dpg.add_text(" X")

                        app_id[f"{i}_x_input_text"] = dpg.add_input_text(
                            label=f"##{i}_x##{APP_NAME}",
                            width=460,
                            hexadecimal=True,
                            no_spaces=True,
                            uppercase=True,
                            user_data=app_id,
                            callback=get_bit_length,
                        )

                        app_id[f"{i}_x_pow"] = dpg.add_text(
                            label=f"##pow##{i}_x##{APP_NAME}"
                        )

                        app_id[f"{i}_get_y_button"] = dpg.add_button(
                            label=f"cal Y##{i}##{APP_NAME}",
                            indent=520,
                            user_data=app_id,
                            callback=get_y_coordinate,
                        )

                    with dpg.group(
                        label=f"group_y_{i}##{APP_NAME}", horizontal=True
                    ) as app_id[f"group_y_{i}"]:
                        dpg.add_text(" Y")

                        app_id[f"{i}_y_input_text"] = dpg.add_input_text(
                            label=f"##{i}_y##{APP_NAME}",
                            width=460,
                            hexadecimal=True,
                            no_spaces=True,
                            uppercase=True,
                            user_data=app_id,
                            callback=get_bit_length,
                        )

                        app_id[f"{i}_y_pow"] = dpg.add_text(
                            label=f"##pow##{i}_y##{APP_NAME}"
                        )

                        app_id[f"{i}_y_neg_y_button"] = dpg.add_button(
                            label=f"y_neg_y_exchange##{i}##{APP_NAME}",
                            indent=520,
                            arrow=True,
                            direction=dpg.mvDir_Down,
                            user_data=app_id,
                            callback=transposition_callback,
                        )

                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text("exchange Y -Y")

                    with dpg.group(
                        label=f"group_neg_y_{i}##{APP_NAME}", horizontal=True
                    ) as app_id[f"group_neg_y_{i}"]:
                        dpg.add_text("-Y")

                        app_id[f"{i}_neg_y_input_text"] = dpg.add_input_text(
                            label=f"##{i}_neg_y##{APP_NAME}",
                            width=460,
                            hexadecimal=True,
                            no_spaces=True,
                            uppercase=True,
                            user_data=app_id,
                            callback=get_bit_length,
                        )

                        app_id[f"{i}_neg_y_pow"] = dpg.add_text(
                            label=f"##pow##{i}_neg_y##{APP_NAME}"
                        )

        with dpg.child_window(width=-1, height=35):
            with dpg.group(horizontal=True):
                dpg.add_text("Operation", color=[255, 0, 0])

                dpg.add_button(
                    label=f"A + B##{APP_NAME}", user_data=app_id, callback=add_callback
                )

                dpg.add_button(
                    label=f"A - B##{APP_NAME}", user_data=app_id, callback=sub_callback
                )

                dpg.add_button(
                    label=f"A * B##{APP_NAME}", user_data=app_id, callback=mul_callback
                )

                dpg.add_button(
                    label=f"A / B##{APP_NAME}", user_data=app_id, callback=div_callback
                )

        with dpg.child_window(width=-1, height=200):
            with dpg.group(label=f"group_C##{APP_NAME}"):
                with dpg.group(horizontal=True):
                    dpg.add_text(" C", color=[255, 0, 0])

                    app_id["C_to_memory_button"] = dpg.add_button(
                        label=f"->Memory##C##{APP_NAME}",
                        indent=448,
                        user_data=app_id,
                        callback=send_to_memory,
                    )

                    app_id["C_clear_button"] = dpg.add_button(
                        label=f"Clear##C##{APP_NAME}",
                        user_data=app_id,
                        callback=clear_callback,
                    )

                with dpg.group(horizontal=True):
                    dpg.add_text(" X")

                    app_id["C_x_input_text"] = dpg.add_input_text(
                        label=f"##C_x##{APP_NAME}",
                        width=460,
                        hexadecimal=True,
                        no_spaces=True,
                        uppercase=True,
                        user_data=app_id,
                        callback=get_bit_length,
                    )

                    app_id["C_x_pow"] = dpg.add_text(label=f"##pow##C_x##{APP_NAME}")

                    app_id["C_x_add_one"] = dpg.add_button(
                        label=f"+##C_x##{APP_NAME}",
                        indent=520,
                        user_data=app_id,
                        callback=add_one_callback,
                    )

                    app_id["C_x_sub_one"] = dpg.add_button(
                        label=f"-##C_x##{APP_NAME}",
                        user_data=app_id,
                        callback=sub_one_callback,
                    )

                with dpg.group(horizontal=True):
                    dpg.add_text(" Y")

                    app_id["C_y_input_text"] = dpg.add_input_text(
                        label=f"##C_y##{APP_NAME}",
                        width=460,
                        hexadecimal=True,
                        no_spaces=True,
                        uppercase=True,
                        user_data=app_id,
                        callback=get_bit_length,
                    )

                    app_id["C_y_pow"] = dpg.add_text(label=f"##pow##C_y##{APP_NAME}")

                with dpg.group(horizontal=True):
                    dpg.add_text("-Y")

                    app_id["C_neg_y_input_text"] = dpg.add_input_text(
                        label=f"##C_neg_y##{APP_NAME}",
                        width=460,
                        hexadecimal=True,
                        no_spaces=True,
                        uppercase=True,
                        user_data=app_id,
                        callback=get_bit_length,
                    )

                    app_id["C_neg_y_pow"] = dpg.add_text(
                        label=f"##pow##C_neg_y##{APP_NAME}"
                    )

            with dpg.group(label=f"group_public_key##{APP_NAME}"):
                with dpg.group(horizontal=True):
                    dpg.add_text("Public key of C:")

                    app_id["public_to_memory_button"] = dpg.add_button(
                        label=f"->Memory##public##{APP_NAME}",
                        indent=448,
                        user_data=app_id,
                        callback=send_to_memory,
                    )

                    app_id["public_clear_button"] = dpg.add_button(
                        label=f"Clear##public##{APP_NAME}",
                        user_data=app_id,
                        callback=clear_callback,
                    )

                with dpg.group(horizontal=True):
                    dpg.add_text(" X")

                    app_id["public_x_input_text"] = dpg.add_input_text(
                        label=f"##public_x##{APP_NAME}",
                        width=460,
                        hexadecimal=True,
                        no_spaces=True,
                        uppercase=True,
                        user_data=app_id,
                        callback=get_bit_length,
                    )

                    app_id["public_x_pow"] = dpg.add_text(
                        label=f"##pow##public_x##{APP_NAME}"
                    )

                with dpg.group(horizontal=True):
                    dpg.add_text(" Y")

                    app_id["public_y_input_text"] = dpg.add_input_text(
                        label=f"##public_y##{APP_NAME}",
                        width=460,
                        hexadecimal=True,
                        no_spaces=True,
                        uppercase=True,
                        user_data=app_id,
                        callback=get_bit_length,
                    )

                    app_id["public_y_pow"] = dpg.add_text(
                        label=f"##pow##public_y##{APP_NAME}"
                    )

                with dpg.group(horizontal=True):
                    dpg.add_text("-Y")

                    app_id["public_neg_y_input_text"] = dpg.add_input_text(
                        label=f"##public_neg_y##{APP_NAME}",
                        width=460,
                        hexadecimal=True,
                        no_spaces=True,
                        uppercase=True,
                        user_data=app_id,
                        callback=get_bit_length,
                    )

                    app_id["public_neg_y_pow"] = dpg.add_text(
                        label=f"##pow##public_neg_y##{APP_NAME}"
                    )

        with dpg.child_window(width=-1, height=35):
            with dpg.group(label=f"group_log##{APP_NAME}"):
                app_id["log_text"] = dpg.add_text(
                    label=f"##log##{APP_NAME}"
                )


    with dpg.window(
        label="Memory",
        width=600,
        height=200,
        pos=[0, 550],
        max_size=[600,800],
        no_scrollbar=True,
        no_close=True,
    ) as app_id["memory"]:
        with dpg.child_window(autosize_x=True, autosize_y=True, no_scrollbar=True):
            clear_memory_buton = dpg.add_button(
                label=f"Clear Memory##{APP_NAME}",
                indent=475,
                user_data=app_id,
                callback=clear_memory,
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
            ) as app_id["memory"]:
                dpg.add_table_column(
                    label="Memory", width_stretch=True, init_width_or_weight=0.0
                )

                dpg.add_table_column(label="Operation", width=10, width_fixed=True)


if __name__ == "__main__":
    dpg.create_viewport(
        title=f"{APP_NAME} {APP_VERSION}", width=610, height=820, x_pos=0, y_pos=0
    )
    add_app_window()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
