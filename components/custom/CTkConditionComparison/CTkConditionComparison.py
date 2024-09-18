from functools import partial
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

        # widgets rendering
        self.redraw_component()
                
    def add_comparison_rule(self) -> None:
        self.row_counter_list.append(len(self.row_counter_list))
        self.redraw_component(row=len(self.row_counter_list) - 1)
        
    def destroy_child_widgets(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        
    def redraw_component(self, row=None) -> None:
        if row is None:
            self.rowconfigure(tuple(self.row_counter_list), weight=1)
            self.destroy_child_widgets()
            for row in self.row_counter_list:
                self.draw_row(row)
        else:
            self.draw_row(row)

    def draw_row(self, row: int) -> None:
        if row == 0:
            CTkLabel(self, text="Condition comparison").grid(row=0, column=0)
            CTkButton(self, text="Add rule", command=self.add_comparison_rule).grid(row=0, column=5)
            CTkButton(self, text="Save", command=self.set_dto).grid(row=0, column=6)
        else:   
            # combobox
            CTkComboBox(self, values=self.selected_comparison_values, 
                        variable=tkinter.StringVar(value=self.conditions.get(row, ""))).grid(row=row, column=0)
            # Checkboxes
            for i, condition in enumerate(self.comparison_values, start=1):
                CTkCheckBox(
                    self, text=condition, 
                    variable=tkinter.StringVar(value=condition if condition in self.condition_comparison_dto.get(self.conditions.get(row, ""), "") else ""),
                    onvalue=condition, offvalue=""
                ).grid(row=row, column=i)
            # button
            CTkButton(self, text="Delete", command=partial(self.delete, row)).grid(row=row, column=6)

    def delete(self, row: int) -> None:
        self.row_counter_list.remove(row)
        for widget in self.winfo_children():
            if widget.grid_info().get("row") == row:
                widget.destroy()
        self.redraw_component()
        
    def set_dto(self)-> None:
        combobox_list = [widget for widget in self.winfo_children() if isinstance(widget, CTkComboBox)]
        checkbox_list = [widget for widget in self.winfo_children() if isinstance(widget, CTkCheckBox)]
        
        if len(combobox_list) == len(checkbox_list):
            for i, widget in combobox_list:
                if widget.grid_info().get("row") == i:
                    self.condition_comparison_dto[widget.get()] = None
            print(self.condition_comparison_dto)
        else:
            pass
                

            