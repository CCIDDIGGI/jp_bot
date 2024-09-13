from enum import Enum
import tkinter
from customtkinter import *
from typing import Any, List

class CtkConditionComparison(CTkFrame):

    def __init__(self, 
                 master: Any,
                 row: int,
                 column: int,
                 columnspan: int,
                 condition_comparison: dict = {}):
        
        self.condition_comparison = condition_comparison
        self.comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        self.selected_comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        self.row_counter_list: list = [0] 
        
        # transfer basic functionality (bg_color, size, appearance_mode, scaling) to CTkBaseClass
        super().__init__(master=master)

        self.grid(row=row, column=column, columnspan=columnspan, sticky='nsew')
        self.columnconfigure((0,1,2,3,4,5), weight=3)
        self.columnconfigure(6, weight=1)

        # widgets     
        # self.lbl_compare = CTkLabel(self, text="Compare...")
        # self.lbl_with = CTkLabel(self, text="with")

        # widgets rendering
        self.redraw_component()

    def check_btn_comparison_status(self, choice) -> None:
        self.condition_comparison[choice] = []
        print(self.condition_comparison[0])
        self.selected_comparison_values.remove(choice)
                
    def add_comparison_rule(self) -> None:
        self.row_counter_list.append(len(self.row_counter_list))
        self.destroy_child_widgets()
        self.redraw_component()
        
    def destroy_child_widgets(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        
    def redraw_component(self) -> None:
        self.rowconfigure(tuple(self.row_counter_list), weight=1)
        for row in self.row_counter_list:
            if row == 0:
                CTkLabel(self, text="Condition comparison").grid(row=0, column=0)
                CTkButton(self, text="Add comparison rule", command=self.add_comparison_rule).grid(row=0, column=6)
            else:   
                CTkComboBox(self, values=self.selected_comparison_values, 
                                                variable=tkinter.StringVar(value=""),
                                                command=self.check_btn_comparison_status).grid(row=row, column=0)
                CTkCheckBox(self, text="NM", variable=self.condition_comparison[ConditionEnum(row)]["NM"], onvalue="NM", offvalue="").grid(row=row, column=1)
                CTkCheckBox(self, text="SP", variable=self.condition_comparison[ConditionEnum(row)]["SP"], onvalue="SP", offvalue="").grid(row=row, column=2)
                CTkCheckBox(self, text="MP", variable=self.condition_comparison[ConditionEnum(row)]["MP"], onvalue="MP", offvalue="").grid(row=row, column=3)
                CTkCheckBox(self, text="PL", variable=self.condition_comparison[ConditionEnum(row)]["PL"], onvalue="PL", offvalue="").grid(row=row, column=4)
                CTkCheckBox(self, text="PO", variable=self.condition_comparison[ConditionEnum(row)]["PO"], onvalue="PO", offvalue="").grid(row=row, column=5)
                CTkButton(self, text="Delete", command=lambda: self.delete(row)).grid(row=row, column=6)

    def delete(self, row: int) -> None:
        self.row_counter_list.remove(row)
        for widget in self.winfo_children():
            if widget.grid_info().get("row") == row:
                widget.destroy()
        self.redraw_component()

class ConditionEnum(Enum):
    NM = 1
    SP = 2
    MP = 3
    PL = 4
    PO = 5
 