import tkinter
from typing import List
from customtkinter import *
from components.custom.CTkConditionComparison.CTkConditionComparison import CtkConditionComparison
from components.custom.CTkScrollableDropdown import CTkScrollableDropdown 

class CreateEditTabView(CTkScrollableFrame):
    
    def __init__(self, parent, is_new_tab: bool):
        self.parent = parent
        
        # main setup
        super().__init__(parent)
        
        self.values = ["Pokémon", "Magic: the Gathering"]
        self.comparison: List[CtkConditionComparison] = []
        self.comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        self.selected_comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        # self.parent.disable_frames()     
        
        if is_new_tab:
            self.configure_new_tab()
        else:
            self.configure_edit_tab()
        
        # widgets callback     
        self.entry_diff_var.trace_add("write", self.try_parse_diff_var)
        self.entry_maximum_threshold_var.trace_add("write", self.try_parse_maximum_threshold_var)

        # widgets rendering  
        self.lbl_name.grid(row=0, column=0, columnspan=1, sticky='w')     
        self.entry_name.grid(row=1, column=0, columnspan=2, sticky='ew')  
        self.lbl_tcg.grid(row=2, column=0, columnspan=2, sticky='w') 
        self.om_tcg.grid(row=3, column=0, columnspan=2, sticky='ew')
        self.lbl_exp.grid(row=2, column=2, sticky='w')
        self.entry_exp.grid(row=3, column=2, sticky='ew')
        self.lbl_diff.grid(row=4, column=0, columnspan=2, sticky='w')    
        self.radio_diff_perc.grid(row=5, column=0, sticky='nsew')
        self.radio_diff_flat.grid(row=5, column=1, sticky='nsew')
        self.entry_diff.grid(row=5, column=2, sticky='ew')  
        self.lbl_comparison.grid(row=7, column=0, columnspan=1, sticky='w')
        self.btn_add_comparison_rule.grid(row=8, column=0, columnspan=1, sticky='w')

        self.btn_cancel.grid(row=13, column=0, columnspan=2, sticky='e')
        self.btn_add.grid(row=13, column=2, sticky='w')

    def configure_new_tab(self) -> None:
        self.configure(fg_color="red", label_text="Add Tab")
        self.grid(row=1, column=1, sticky='nsew')
        self.grid_columnconfigure((0,1), weight=1, uniform='column')
        self.grid_columnconfigure(2, weight=2, uniform='column')
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=3, uniform='row')
        self.grid_rowconfigure(13, weight=1, uniform='row')

        self.radio_diff_var = tkinter.IntVar(value=1)
        self.entry_diff_var = tkinter.StringVar(value='10')
        self.entry_maximum_threshold_var = tkinter.StringVar(value='50')
        
        # widgets
        self.lbl_name = CTkLabel(self, text="Enter tab name") 
        self.entry_name = CTkEntry(self)
        self.lbl_tcg = CTkLabel(self, text="Choose a TCG") 
        self.om_tcg = CTkOptionMenu(self)
        self.drpd_tcg = CTkScrollableDropdown(self.om_tcg,
                                        values=self.values,
                                        command=self.get_expansions_by_tcg)  
        
        self.lbl_exp = CTkLabel(self, text="Choose an expansion from the list") 
        self.entry_exp = CTkEntry(self)
        self.drpd_exp = CTkScrollableDropdown(self.entry_exp,
                                              command=lambda e: 
                                                  self.entry_exp.delete(0,'end') 
                                                  or self.entry_exp.insert(0, e),
                                              autocomplete=True) 
        self.btn_cancel = CTkButton(self, text="Cancel", command=self.cancel_procedure)
        self.btn_add = CTkButton(self, text="Add", command=self.add_new_tab)

        self.lbl_diff = CTkLabel(self, text="Minimum price difference") 
        self.radio_diff_perc = CTkRadioButton(self, text="Percentage", variable=self.radio_diff_var, value=1)
        self.radio_diff_flat = CTkRadioButton(self, text="Flat value", variable=self.radio_diff_var, value=2)
        self.entry_diff = CTkEntry(self, textvariable=self.entry_diff_var)
        self.lbl_diff_err = CTkLabel(self, text="Please insert only numerical values!")

        self.lbl_comparison = CTkLabel(self, text="Condition comparison") 
        self.btn_add_comparison_rule = CTkButton(self, text="Add comparison rule", command=self.add_comparison_rule)

        self.lbl_maximum_threshold = CTkLabel(self, text="Maximum threshold amount (EUR) that the software can add to the cart")
        self.entry_maximum_threshold = CTkEntry(self, textvariable=self.entry_maximum_threshold_var)       
        self.lbl_maximum_threshold_err = CTkLabel(self, text="Please insert only numerical values!")
        
    def configure_edit_tab(self) -> None:
        self.configure(fg_color = "red", label_text="Edit Tab")
        self.grid(row=1, column=1, sticky='nsew')
        self.grid_columnconfigure((0,1), weight=1, uniform='column')
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=3, uniform='row')
        self.grid_rowconfigure(9, weight=1, uniform='row')

        self.radio_diff_var = tkinter.IntVar(value=1)
        self.entry_diff_var = tkinter.StringVar(value='10')
        self.entry_maximum_threshold_var = tkinter.StringVar(value='50')
        
        # widgets
        self.lbl_name = CTkLabel(self, text="Enter a tab name") 
        self.entry_name = CTkEntry(self)
        self.lbl_tcg = CTkLabel(self, text="Choose a TCG") 
        self.om_tcg = CTkOptionMenu(self)
        self.drpd_tcg = CTkScrollableDropdown(self.om_tcg,
                                        values=self.values,
                                        command=self.get_expansions_by_tcg)  
        
        self.lbl_exp = CTkLabel(self, text="Choose an expansion from the list") 
        self.entry_exp = CTkEntry(self)
        self.drpd_exp = CTkScrollableDropdown(self.entry_exp,
                                              command=lambda e: 
                                                  self.entry_exp.delete(0,'end') 
                                                  or self.entry_exp.insert(0, e),
                                              autocomplete=True) 
        self.btn_cancel = CTkButton(self, text="Cancel", command=self.cancel_procedure)
        self.btn_add = CTkButton(self, text="Add", command=self.add_new_tab)

        self.lbl_diff = CTkLabel(self, text="Minimum price difference between the first and second cheapest listings", wraplength=200) 
        self.radio_diff_perc = CTkRadioButton(self, text="Percentage", variable=self.radio_diff_var, value=1 )
        self.radio_diff_flat = CTkRadioButton(self, text="Flat value", variable=self.radio_diff_var, value=2 )
        self.entry_diff = CTkEntry(self)

    def set_controller(self, controller) -> None:
        self.controller = controller

    def init_get_exp(self) -> None:
        self.get_expansions_by_tcg(self.values[0])

    def get_expansions_by_tcg(self, choice: str) -> None:
        self.controller.get_expansions_by_tcg(choice)
        self.om_tcg.set(choice)

    def set_expansions_by_tcg(self, exp: list) -> None:
        self.drpd_exp.configure(values=exp)

    def try_parse_diff_var(self, *args) -> None:
        try:
            self.diff_value = int(self.entry_diff_var.get()) if self.entry_diff_var.get() else 0
            self.lbl_diff_err.grid_remove()
        except ValueError:
            self.lbl_diff_err.grid(row=6, column=2, sticky='w')
            
    def try_parse_maximum_threshold_var(self, *args) -> None:
        try:
            self.maximum_threshold_value = int(self.entry_maximum_threshold_var.get()) if self.entry_maximum_threshold_var.get() else 0
            self.lbl_maximum_threshold_err.grid_remove()
        except ValueError:
            self.lbl_maximum_threshold_err.grid(row=6, column=2, sticky='w')

    def add_comparison_rule(self) -> None:
        if len(self.comparison) >= 1:
            for filter in self.comparison:
                if filter.cmb_left_condition_var.get() in self.selected_comparison_values:
                    self.selected_comparison_values.remove(filter.cmb_left_condition_var.get())

        self.comparison.append(CtkConditionComparison(self, row=(9+len(self.comparison)), 
                                                    column=0, columnspan=3, 
                                                    values=self.selected_comparison_values))
        self.check_btn_comparison_status()
            
    def delete_comparison_rule(self, comparison_rule: CtkConditionComparison) -> None:
        self.comparison.remove(comparison_rule)
        self.check_btn_comparison_status()

            
    def check_btn_comparison_status(self) -> None:
        self.btn_add_comparison_rule.configure(state="normal" if all(filter.cmb_left_condition_var.get() != "" for 
                                                                     filter in self.comparison) and len(self.comparison) < 5 or
                                                                     len(self.comparison) == 0
                                                                     else "disabled")

        
    def cancel_procedure(self) -> None:
        # self.parent.enable_frames()
        self.controller.cancel_procedure()
        self.grid_remove()
    
    def add_new_tab(self) -> None:
        tab_dto = {
            "name": self.entry_name.get()
        }
        
        self.controller.add_new_tab(tab_dto)
        self.cancel_procedure()