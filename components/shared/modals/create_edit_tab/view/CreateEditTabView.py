import tkinter
from customtkinter import *
from components.custom.CTkScrollableDropdown import CTkScrollableDropdown
from components.tabs.dto.tab_dto import TabDTO

class CreateEditTabView(CTkScrollableFrame):

    def __init__(self, parent, tab_data: TabDTO = TabDTO(
            name = None,
            tcg = None,
            expansion = None,
            price_difference_type = None,
            price_difference = None,
            condition_comparison = {},
            maximum_threshold = None
    )):
        self.parent = parent
        self.tab_dto: TabDTO = tab_data
        self.diff_value = 10
        self.maximum_threshold_value = 50

        # main setup
        super().__init__(parent)
         
        self.configure(fg_color="#333333", label_text="Edit Tab" if self.tab_dto.name else "Add Tab")
        self.grid(row=1, column=1, sticky='nsew')
        self.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1, uniform='column')
        self.grid_rowconfigure((0,1,2,3,4,5,6,8,9,10,11,13,14,15,16,17), weight=1, uniform='row')
        self.grid_rowconfigure(7, weight=3, uniform='row')
        # self.parent.disable_frames()
        
        self.values = ["Pokémon", "Magic: the Gathering"]
        self.conditions: dict = { 1: "NM", 2: "SP", 3: "MP", 4: "PL", 5: "PO" }
        self.condition_comparison_dict: dict = dict(self.tab_dto.condition_comparison)
        self.entry_name_var = tkinter.StringVar(value=self.tab_dto.name if self.tab_dto.name else "")
        self.entry_exp_var = tkinter.StringVar(value=self.tab_dto.expansion if self.tab_dto.expansion else "") 
        self.radio_diff_var = tkinter.IntVar(value=self.tab_dto.price_difference_type if self.tab_dto.price_difference_type else 1)
        self.entry_diff_var = tkinter.StringVar(value=self.tab_dto.price_difference if self.tab_dto.price_difference else '10')
        self.entry_maximum_threshold_var = tkinter.StringVar(value=self.tab_dto.maximum_threshold if self.tab_dto.maximum_threshold else '50')

        # widgets
        self.lbl_name = CTkLabel(self, text="Enter tab name")
        self.entry_name = CTkEntry(self, textvariable=self.entry_name_var)
        self.lbl_tcg = CTkLabel(self, text="Choose a TCG")
        self.om_tcg = CTkOptionMenu(self)
        self.drpd_tcg = CTkScrollableDropdown(self.om_tcg,
                                        values=self.values,
                                        command=self.get_expansions_by_tcg)

        self.lbl_exp = CTkLabel(self, text="Choose an expansion from the list")
        self.entry_exp = CTkEntry(self)
        self.drpd_exp = CTkScrollableDropdown(self.entry_exp,
                                              command=self.set_drpd,
                                              autocomplete=True)
        self.lbl_diff = CTkLabel(self, text="Minimum price difference")
        self.radio_diff_perc = CTkRadioButton(self, text="Percentage", variable=self.radio_diff_var, value=1)
        self.radio_diff_flat = CTkRadioButton(self, text="Flat value", variable=self.radio_diff_var, value=2)
        self.entry_diff = CTkEntry(self, textvariable=self.entry_diff_var)
        self.lbl_diff_err = CTkLabel(self, text="Please insert only numerical values!", text_color="red")
        CTkLabel(self, text="Condition comparison").grid(row=7, column=0, columnspan=6, sticky='w')
        for row in range(1, 6):
            CTkLabel(self, text=self.conditions[row]).grid(row=7+row, column=0)
            for col in range(1, 6):
                CTkCheckBox(self, text=self.conditions[col],
                            variable=tkinter.StringVar(value=self.get_value(row, col)),
                            onvalue=self.conditions[col], 
                            offvalue="",
                            command=lambda r=7+row, c=col: self.set_dto(r, c)).grid(row=7+row, column=col)
        self.lbl_maximum_threshold = CTkLabel(self, text="Maximum threshold amount")
        self.entry_maximum_threshold = CTkEntry(self, textvariable=self.entry_maximum_threshold_var)
        self.lbl_maximum_threshold_err = CTkLabel(self, text="Please insert only numerical values!", text_color="red")
        self.lbl_form_error = CTkLabel(self, text="Please fill all the fields",  text_color="red")
        self.btn_cancel = CTkButton(self, text="Cancel", command=self.cancel_procedure)
        self.btn_add = CTkButton(self, text="Add", command=self.add_new_tab)
        
        # widgets callback
        self.entry_diff_var.trace_add("write", self.try_parse_diff_var)
        self.entry_maximum_threshold_var.trace_add("write", self.try_parse_maximum_threshold_var)
        if self.tab_dto.expansion:
            self.set_drpd(self.tab_dto.expansion)

        # widgets rendering
        self.lbl_name.grid(row=0, column=0, columnspan=6, sticky='w')
        self.entry_name.grid(row=1, column=0, columnspan=4, sticky='ew')
        self.lbl_tcg.grid(row=2, column=0, columnspan=6, sticky='w')
        self.om_tcg.grid(row=3, column=0, columnspan=4, sticky='ew')
        self.lbl_exp.grid(row=2, column=4, columnspan=4, sticky='w')
        self.entry_exp.grid(row=3, column=4, columnspan=4, sticky='ew')
        self.lbl_diff.grid(row=4, column=0, columnspan=6, sticky='w')
        self.radio_diff_perc.grid(row=5, column=0, columnspan=2, sticky='nsew')
        self.radio_diff_flat.grid(row=5, column=2, columnspan=2, sticky='nsew')
        self.entry_diff.grid(row=5, column=4, columnspan=4, sticky='ew')
        self.lbl_maximum_threshold.grid(row=13, column=0, columnspan=6, sticky='w')
        self.entry_maximum_threshold.grid(row=14, column=0, columnspan=4, sticky='ew')
        self.btn_cancel.grid(row=17, column=3, sticky='e')
        self.btn_add.grid(row=17, column=4, sticky='w')

    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def set_drpd(self, exp: str) -> None:
        self.entry_exp.delete(0, 'end')
        self.entry_exp.insert(0, exp)

    def set_dto(self, row: int, col: int) -> None:
        condition_row = self.conditions[row-7]
        condition_col = self.conditions[col]
        if condition_row not in self.condition_comparison_dict:
            self.condition_comparison_dict[condition_row] = []

        for widget in self.winfo_children():
            if isinstance(widget, CTkCheckBox):
                if widget.grid_info().get("row") == row and widget.grid_info().get("column") == col:
                    if condition_col in self.condition_comparison_dict[condition_row]:
                        self.condition_comparison_dict[condition_row].remove(condition_col)
                    else:
                        self.condition_comparison_dict[condition_row].append(condition_col)

    def init_get_exp(self) -> None:
        self.get_expansions_by_tcg(self.tab_dto.tcg if self.tab_dto.tcg else self.values[0])

    def get_expansions_by_tcg(self, choice: str) -> None:
        self.controller.get_expansions_by_tcg(choice)
        self.om_tcg.set(choice)

    def get_value(self, row: int, col: int) -> str:
        row_condition = self.conditions[row]
        col_condition = self.conditions[col]

        if row_condition in self.tab_dto.condition_comparison:
            if col_condition in self.tab_dto.condition_comparison[row_condition]:
                return col_condition
            else:
                return ""
        else:
            return ""

    def set_expansions_by_tcg(self, exp: list) -> None:
        self.drpd_exp.configure(values=exp)

    def try_parse_diff_var(self, *args) -> None:
        try:
            self.diff_value = int(self.entry_diff_var.get()) if self.entry_diff_var.get() else 0
            self.lbl_diff_err.grid_remove()
        except ValueError:
            self.lbl_diff_err.grid(row=6, column=4, columnspan=4, sticky='w')

    def try_parse_maximum_threshold_var(self, *args) -> None:
        try:
            self.maximum_threshold_value = int(self.entry_maximum_threshold_var.get()) if self.entry_maximum_threshold_var.get() else 0
            self.lbl_maximum_threshold_err.grid_remove()
        except ValueError:
            self.lbl_maximum_threshold_err.grid(row=15, column=0, columnspan=4, sticky='w')

    def cancel_procedure(self) -> None:
        self.controller.cancel_procedure()

    def add_new_tab(self) -> None:
        if all([
            self.entry_name.get(),
            self.om_tcg.get(),
            self.entry_exp.get(),
            self.diff_value,
            self.entry_diff_var.get(),
            self.condition_comparison_dict,
            self.maximum_threshold_value
        ]):
            self.tab_dto = TabDTO(
                name = self.entry_name.get(),
                tcg = self.om_tcg.get(),
                expansion = self.entry_exp.get(),
                price_difference_type = self.diff_value,
                price_difference = self.entry_diff_var.get(),
                condition_comparison = self.condition_comparison_dict,
                maximum_threshold = self.maximum_threshold_value
            )
            self.controller.add_new_tab(self.tab_dto)
            self.cancel_procedure()
        else:
            self.lbl_form_error.grid(row=16, column=0, columnspan=4, sticky='w')
