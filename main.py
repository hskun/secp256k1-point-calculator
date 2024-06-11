import dearpygui.dearpygui as dpg
from lib.callback import *
import BigIntCal as BigInt

dpg.create_context()

APP_NAME = "secp256k1 point Calculator"
APP_VERSION = "1.3"
app_id = dict()
memory_data = dict()


def add_app_window():
    with dpg.window(
        label=f"{APP_NAME} {APP_VERSION}",
        width=600,
        height=575,
        pos=[0, 0],
        min_size=[600, 575],
        no_resize=True,
        no_move=True,
        no_close=True,
        # no_collapse=True,
        # no_title_bar=True,
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
            with dpg.menu(label="Tools"):
                dpg.add_menu_item(
                    label="BigInt Calculator", callback=lambda: BigInt.BigInt_window()
                )


        for i in "AB":
            with dpg.child_window(width=-1, height=110, no_scrollbar=True):
                with dpg.group(label=f"group_{i}##{APP_NAME}"):
                    with dpg.group(horizontal=True):
                        with dpg.table(
                            header_row=False,
                            borders_innerH=False,
                            borders_innerV=False,
                            borders_outerH=False,
                        ) as app_id[f"table_option_{i}"]:
                            dpg.add_table_column(width=10, width_fixed=True)
                            dpg.add_table_column(
                                width_stretch=True, init_width_or_weight=0.0
                            )
                            dpg.add_table_column(width_fixed=True)

                            with dpg.table_row():

                                dpg.add_text(f" {i}", color=[255, 0, 0])
                                app_id[f"{i}_radio_button"] = dpg.add_radio_button(
                                    label=f"radio##{i}##{APP_NAME}",
                                    items=("Vector", "Scalar"),
                                    default_value="Vector",
                                    horizontal=True,
                                    user_data=app_id,
                                    callback=select_type,
                                )

                                with dpg.group(horizontal=True):
                                    app_id[f"{i}_rand_button"] = dpg.add_button(
                                        label=f"Rand##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=rand_callback,
                                    )
                                    app_id[f"{i}_base_point_button"] = dpg.add_button(
                                        label=f"Base Point##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=base_point_callback,
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
                                        user_data=app_id,
                                        callback=send_to_memory,
                                    )
                                    app_id[f"{i}_clear_button"] = dpg.add_button(
                                        label=f"Clear##{i}##{APP_NAME}",
                                        user_data=app_id,
                                        callback=clear_callback,
                                    )

                    with dpg.table(
                        label=f"table_{i}##{APP_NAME}",
                        # width=-1,
                        header_row=False,
                        borders_innerH=False,
                        borders_outerH=False,
                        borders_innerV=False,
                    ) as app_id[f"table_{i}"]:
                        dpg.add_table_column(width_fixed=True)
                        dpg.add_table_column(width_fixed=True)
                        dpg.add_table_column(
                            width_stretch=True, init_width_or_weight=0.0
                        )
                        dpg.add_table_column(width_fixed=True)

                        with dpg.table_row():
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
                                label=f"Cal Y##{i}##{APP_NAME}",
                                # width=50,
                                user_data=app_id,
                                callback=get_y_coordinate,
                            )

                        with dpg.table_row(label=f"table_{i}_y##{APP_NAME}") as app_id[
                            f"table_{i}_y"
                        ]:
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
                                arrow=True,
                                direction=dpg.mvDir_Down,
                                user_data=app_id,
                                callback=transposition_callback,
                            )
                            with dpg.tooltip(dpg.last_item()):
                                dpg.add_text("exchange Y -Y")

                        with dpg.table_row(
                            label=f"table_{i}_neg_y##{APP_NAME}"
                        ) as app_id[f"table_{i}_neg_y"]:
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
                            dpg.add_table_cell()

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

        with dpg.child_window(width=-1, height=215):
            with dpg.group(label=f"group_C##{APP_NAME}"):
                with dpg.group(horizontal=True):
                    with dpg.table(
                        header_row=False,
                        borders_innerH=False,
                        borders_innerV=False,
                        borders_outerH=False,
                    ) as app_id[f"table_option_{i}"]:
                        dpg.add_table_column(
                            width_stretch=True, init_width_or_weight=0.0
                        )
                        dpg.add_table_column(width_fixed=True)

                        with dpg.table_row():
                            dpg.add_text(" C", color=[255, 0, 0])
                            with dpg.group(horizontal=True):
                                app_id["C_to_memory_button"] = dpg.add_button(
                                    label=f"->Memory##C##{APP_NAME}",
                                    user_data=app_id,
                                    callback=send_to_memory,
                                )
                                app_id["C_clear_button"] = dpg.add_button(
                                    label=f"Clear##C##{APP_NAME}",
                                    user_data=app_id,
                                    callback=clear_callback,
                                )

                with dpg.table(
                    label=f"table_C##{APP_NAME}",
                    header_row=False,
                    borders_innerH=False,
                    borders_outerH=False,
                    borders_innerV=False,
                    borders_outerV=False,
                ) as app_id[f"table_C"]:
                    dpg.add_table_column(width=10, width_fixed=True)
                    dpg.add_table_column(width=460, width_fixed=True)
                    dpg.add_table_column(width_stretch=True, init_width_or_weight=0.0)
                    dpg.add_table_column(width=43, width_fixed=True)

                    with dpg.table_row():
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
                        app_id["C_x_pow"] = dpg.add_text(
                            label=f"##pow##C_x##{APP_NAME}"
                        )
                        with dpg.group(horizontal=True):
                            app_id["C_x_sub_one"] = dpg.add_button(
                                # arrow=True,
                                # direction=dpg.mvDir_Left,
                                label=f"-##C_x##{APP_NAME}",
                                user_data=app_id,
                                callback=sub_one_callback,
                            )
                            app_id["C_x_add_one"] = dpg.add_button(
                                # arrow=True,
                                # direction=dpg.mvDir_Right,
                                label=f"+##C_x##{APP_NAME}",
                                user_data=app_id,
                                callback=add_one_callback,
                            )

                    with dpg.table_row():
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
                        app_id["C_y_pow"] = dpg.add_text(
                            label=f"##pow##C_y##{APP_NAME}"
                        )
                        dpg.add_table_cell()

                    with dpg.table_row():
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
                        dpg.add_table_cell()

            with dpg.group(label=f"group_public_key##{APP_NAME}") as app_id[
                f"group_public_key"
            ]:
                with dpg.group(horizontal=True):
                    with dpg.table(
                        header_row=False,
                        borders_innerH=False,
                        borders_innerV=False,
                        borders_outerH=False,
                    ):
                        dpg.add_table_column(
                            width_stretch=True, init_width_or_weight=0.0
                        )
                        dpg.add_table_column(width_fixed=True)

                        with dpg.table_row():
                            dpg.add_text("Public key of C.x")
                            with dpg.group(horizontal=True):
                                app_id["public_to_memory_button"] = dpg.add_button(
                                    label=f"->Memory##public##{APP_NAME}",
                                    user_data=app_id,
                                    callback=send_to_memory,
                                )
                                app_id["public_clear_button"] = dpg.add_button(
                                    label=f"Clear##public##{APP_NAME}",
                                    user_data=app_id,
                                    callback=clear_callback,
                                )

                with dpg.table(
                    label=f"table_public_key##{APP_NAME}",
                    header_row=False,
                    borders_innerH=False,
                    borders_outerH=False,
                    borders_innerV=False,
                    borders_outerV=False,
                ) as app_id[f"table_C"]:
                    dpg.add_table_column(width=10, width_fixed=True)
                    dpg.add_table_column(width=460, width_fixed=True)
                    dpg.add_table_column(width_stretch=True, init_width_or_weight=0.0)
                    dpg.add_table_column(width_fixed=True)

                    with dpg.table_row():
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
                        dpg.add_table_cell()

                    with dpg.table_row():
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
                        dpg.add_table_cell()

                    with dpg.table_row():
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
                        dpg.add_table_cell()

        with dpg.child_window(width=-1, height=35):
            with dpg.group(label=f"group_log##{APP_NAME}"):
                app_id["log_text"] = dpg.add_text(label=f"##log##{APP_NAME}")

    with dpg.window(
        label="Memory",
        width=600,
        height=320,
        pos=[0, 575],
        min_size=[600, 320],
        max_size=[600, 2000],
        no_scrollbar=True,
        no_close=True,
    ) as app_id["memory"]:
        with dpg.child_window(autosize_x=True, autosize_y=True, no_scrollbar=True):
            with dpg.table(
                header_row=False,
                borders_innerH=False,
                borders_outerH=False,
                borders_innerV=False,
            ):
                dpg.add_table_column(width_stretch=True, init_width_or_weight=0.0)
                dpg.add_table_column(width_fixed=True)

                with dpg.table_row():
                    dpg.add_table_cell()
                    clear_memory_buton = dpg.add_button(
                        label=f"Clear All##{APP_NAME}",
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
                tag="memory_table",
            ) as app_id["memory"]:
                dpg.add_table_column(
                    label="Memory", width_stretch=True, init_width_or_weight=0.0
                )

                dpg.add_table_column(label="Operation", width=10, width_fixed=True)


if __name__ == "__main__":
    dpg.create_viewport(
        title=APP_NAME, width=600, height=900, x_pos=0, y_pos=0
    )
    add_app_window()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

