import asyncio
import threading
from customtkinter import *

class LoadingScreenService(CTkFrame): 

    # child of MainView -> parent argument is MainView
    def __init__(self, parent): 
        self.parent = parent
        
    def render_loading_screen(self) -> None:
        # main setup
        super().__init__(self.parent)
        self.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="nsew")
        self.grid_rowconfigure((0,6), weight=1, uniform="loading")
        self.grid_rowconfigure((1,5), weight=5, uniform="loading")
        self.grid_columnconfigure((0,6), weight=1, uniform="loading")
        self.grid_columnconfigure((1,5), weight=5, uniform="loading")
  
        # widgets      
        self.lbl_loading = CTkLabel(self, text="Loading...")
        self.lbl_dot_0 = CTkLabel(self, corner_radius=50, fg_color="red")
        self.lbl_dot_1 = CTkLabel(self, corner_radius=50, fg_color="red")
        self.lbl_dot_2 = CTkLabel(self, corner_radius=50, fg_color="red")
        self.lbl_dot_3 = CTkLabel(self, corner_radius=50, fg_color="red")
        self.lbl_dot_4 = CTkLabel(self, corner_radius=50, fg_color="red")
        self.lbl_dot_5 = CTkLabel(self, corner_radius=50, fg_color="red")
        self.lbl_dot_6 = CTkLabel(self, corner_radius=50, fg_color="red")
        self.lbl_dot_7 = CTkLabel(self, corner_radius=50, fg_color="red")
        
        # widgets rendering
        self.lbl_loading.grid(row=0, column=1, columnspan=4)
        self.lbl_dot_0.grid(row=1, column=3)
        self.lbl_dot_1.grid(row=2, column=4)
        self.lbl_dot_2.grid(row=3, column=5)
        self.lbl_dot_3.grid(row=4, column=4)
        self.lbl_dot_4.grid(row=5, column=3)
        self.lbl_dot_5.grid(row=4, column=2)
        self.lbl_dot_6.grid(row=3, column=1)
        self.lbl_dot_7.grid(row=2, column=2)
        
    async def start_loading(self) -> None:
        print("created")
        self.parent.after(0, self.render_loading_screen)
        
    async def stop_loading(self) -> None:
        print("destriyed")
        self.parent.after(0, self.grid_forget)
        
    def run_async_start(self) -> None:
        asyncio.run(self.start_main())
        
    async def start_main(self) -> None:
        await self.start_loading()
        
    def run_async_stop(self) -> None:
        asyncio.run(self.stop_main())
        
    async def stop_main(self) -> None:
        await self.stop_loading()
        
    def start_loading_sequence(self) -> None:
        thread_start = threading.Thread(target=self.run_async_start)
        thread_start.start()  
        thread_start.join()
        
    def stop_loading_sequence(self) -> None:
        thread_stop = threading.Thread(target=self.run_async_stop)
        thread_stop.start()
        