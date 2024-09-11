import tkinter
from customtkinter import *
from typing import Any, List

class CtkConditionComparison(CTkFrame):

    def __init__(self, 
                 master: Any,
                 row: int,
                 column: int,
                 columnspan: int,
                 dto: List[str] = []):
        
        self.comparison: List[CtkConditionComparison] = []
        self.comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        self.selected_comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        
        # transfer basic functionality (bg_color, size, appearance_mode, scaling) to CTkBaseClass
        super().__init__(master=master)

        self.grid(row=row, column=column, columnspan=columnspan, sticky='nsew')
        self.columnconfigure((0,1,2,3,4,5), weight=3)
        self.columnconfigure(6, weight=1)
        self.rowconfigure((0,1,2,3), weight=1)

        self.cmb_left_condition_var = tkinter.StringVar(value="")

        # widgets     
        self.lbl_comparison = CTkLabel(self, text="Condition comparison") 
        self.btn_add_comparison_rule = CTkButton(self, text="Add comparison rule", command=self.add_comparison_rule)
        self.lbl_compare = CTkLabel(self, text="Compare...")
        self.lbl_with = CTkLabel(self, text="with")

        self.cmb_left_condition = CTkComboBox(self, values=values, 
                                              variable=self.cmb_left_condition_var,
                                              command=self.check_btn_comparison_status)
        
        self.cbx_nm = CTkCheckBox(self, text="NM")
        self.cbx_sp = CTkCheckBox(self, text="SP")
        self.cbx_mp = CTkCheckBox(self, text="MP")
        self.cbx_pl = CTkCheckBox(self, text="PL")
        self.cbx_po = CTkCheckBox(self, text="PO")

        self.btn_delete = CTkButton(self, text="Delete", command=self.delete)

        # widgets rendering
        self.lbl_compare.grid(row=0, column=0)
        self.lbl_with.grid(row=0, column=1, columnspan=4)
        self.cmb_left_condition.grid(row=1, column=0)
        self.cbx_nm.grid(row=1, column=1)
        self.cbx_sp.grid(row=1, column=2)
        self.cbx_mp.grid(row=1, column=3)
        self.cbx_pl.grid(row=1, column=4)
        self.cbx_po.grid(row=1, column=5)
        self.btn_delete.grid(row=1, column=6)

    def check_btn_comparison_status(self, *kwargs) -> None:
        self.master.check_btn_comparison_status()

    def delete(self) -> None:
        self.master.delete_comparison_rule(self)
        self.destroy()




 