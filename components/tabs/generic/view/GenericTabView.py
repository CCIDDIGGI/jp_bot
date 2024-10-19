import asyncio
from customtkinter import *
from components.tabs.dto.tab_dto import TabDTO

class GenericTabView(CTkFrame):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.configure(fg_color = "transparent")
        
        self.grid(row=1, column=1)
        # self.grid_columnconfigure
        # self.grid_rowconfigure
            
        # widgets
        self.lbl_info_tcg = CTkLabel(self)
        self.lbl_info_exp = CTkLabel(self)
        self.lbl_info_diff = CTkLabel(self)
        
        self.btn_edit_tab = CTkButton(self, text="Edit this tab", command=self.edit_tab)
        self.btn_delete_tab = CTkButton(self, text="Delete this tab", command=self.delete_tab)
        
        self.btn_start_process = CTkButton(self, text="Start process", command=self.start_process_wrapper)
        self.btn_stop_process = CTkButton(self, text="Stop process", command=self.stop_process)

       
        # widgets rendering
        self.lbl_info_tcg.grid(row=1, column=1, columnspan=3)
        self.lbl_info_exp.grid(row=2, column=1, columnspan=3)
        self.lbl_info_diff.grid(row=3, column=1, columnspan=3)
        
        self.btn_edit_tab.grid(row=4, column=1)
        self.btn_delete_tab.grid(row=4, column=2)        
        
        self.btn_start_process.grid(row=5, column=1)
        self.btn_stop_process.grid(row=5, column=2)

        
    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def init_user_info(self, tab_dto: TabDTO) -> None:
        self.lbl_info_tcg.configure(text=f"from tcg: {tab_dto.tcg}")
        self.lbl_info_exp.configure(text=f"fetch all cards from expansion: {tab_dto.expansion}")
        self.lbl_info_diff.configure(text=f"which price is at least {tab_dto.price_difference} cheaper than the second cheapest listing")

    def delete_tab(self) -> None:
        self.controller.delete_tab()
                
    def edit_tab(self) -> None:
        self.controller.edit_tab()
        
    def redraw_tab(self, tab_dto: TabDTO) -> None:
        pass
    
    def start_process_wrapper(self):
        asyncio.run(self.start_process())
    
    async def start_process(self) -> None:
        await self.controller.start_process()
    
    def stop_process(self) -> None:
        self.controller.stop_process()