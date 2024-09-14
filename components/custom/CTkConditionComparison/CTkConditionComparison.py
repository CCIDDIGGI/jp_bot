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
        
        self.condition_comparison_dto = condition_comparison
        self.comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        self.selected_comparison_values: List[str] = ["NM", "SP", "MP", "PL", "PO"]
        self.conditions: dict = { 1: "NM", 2: "SP", 3: "MP", 4: "PL", 5: "PO" }
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
        self.condition_comparison_dto[choice] = []
        print(self.condition_comparison_dto[0])
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
                                                variable=tkinter.StringVar(value=self.conditions[row] if self.conditions[row] in self.condition_comparison_dto else ""),
                                                command=self.check_btn_comparison_status).grid(row=row, column=0)
                CTkCheckBox(self, text="NM", variable= tkinter.StringVar(value="NM" if "NM" in self.condition_comparison_dto.get(self.conditions[row], "") else ""),
                            onvalue="NM", offvalue="").grid(row=row, column=1)
                CTkCheckBox(self, text="SP", variable= tkinter.StringVar(value="SP" if "SP" in self.condition_comparison_dto.get(self.conditions[row], "") else ""),
                            onvalue="SP", offvalue="").grid(row=row, column=2)
                CTkCheckBox(self, text="MP", variable= tkinter.StringVar(value="MP" if "MP" in self.condition_comparison_dto.get(self.conditions[row], "") else ""),
                            onvalue="MP", offvalue="").grid(row=row, column=3)
                CTkCheckBox(self, text="PL", variable= tkinter.StringVar(value="PL" if "PL" in self.condition_comparison_dto.get(self.conditions[row], "") else ""),
                            onvalue="PL", offvalue="").grid(row=row, column=4)
                CTkCheckBox(self, text="PO", variable= tkinter.StringVar(value="PO" if "PO" in self.condition_comparison_dto.get(self.conditions[row], "") else ""),
                            onvalue="PO", offvalue="").grid(row=row, column=5)
                CTkButton(self, text="Delete", command=lambda: self.delete(row)).grid(row=row, column=6)

    def delete(self, row: int) -> None:
        self.row_counter_list.remove(row)
        del self.condition_comparison_dto[self.conditions[row]]
        for widget in self.winfo_children():
            if widget.grid_info().get("row") == row:
                widget.destroy()
        self.redraw_component()
 