from functools import partial
import tkinter
from customtkinter import *
from typing import Any


class CtkConditionComparison(CTkFrame):

    def __init__(self, 
                 master: Any,
                 row: int,
                 column: int,
                 columnspan: int,
                 condition_comparison: dict = {}):
        
        self.condition_comparison_dto = condition_comparison
        self.conditions: dict = { 1: "NM", 2: "SP", 3: "MP", 4: "PL", 5: "PO" }
        
        # transfer basic functionality (bg_color, size, appearance_mode, scaling) to CTkBaseClass
        super().__init__(master=master)

        self.grid(row=row, column=column, columnspan=columnspan, sticky='nsew')
        self.columnconfigure((0,1,2,3,4,5), weight=3)
        self.columnconfigure(6, weight=1)

        # widgets rendering
        self.draw()

    def draw(self) -> None:
        CTkLabel(self, text="Condition comparison").grid(row=0, column=0)
        
        for row in range(1, 6):
            CTkLabel(self, text=self.conditions[row]).grid(row=row, column=0)
            for col in range(1, 6):
                CTkCheckBox(self, text=self.conditions[col],
                            variable=tkinter.StringVar(value=self.conditions[col] if self.conditions[col] in self.condition_comparison_dto.get(self.conditions.get(row, ""), "") else ""),
                            onvalue=self.conditions[col], 
                            offvalue="",
                            command=lambda r=row, c=col: self.set_dto(r, c)).grid(row=row, column=col)
        
    def set_dto(self, row: int, col: int) -> None:
        condition_row = self.conditions[row]
        condition_col = self.conditions[col]

        if condition_row not in self.condition_comparison_dto:
            self.condition_comparison_dto[condition_row] = []

        for widget in self.winfo_children():
            if isinstance(widget, CTkCheckBox):
                if widget.grid_info().get("row") == row and widget.grid_info().get("column") == col:
                    if condition_col in self.condition_comparison_dto[condition_row]:
                        self.condition_comparison_dto[condition_row].remove(condition_col)
                    else:
                        self.condition_comparison_dto[condition_row].append(condition_col)
                
    def get_dto(self) -> dict:
        return self.condition_comparison_dto
    
    def destroy(self) -> None:
        print("killed")
        super().destroy()
    
            