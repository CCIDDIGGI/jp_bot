from customtkinter import *

class SidebarView(CTkFrame):

    # child of MainView -> parent argument is MainView
    def __init__(self, parent):

        # main setup
        super().__init__(parent)
        self.place(relx = 0, rely = 0, relwidth = 0.25, relheight = 1)

        # widgets
        lbl_filters = CTkLabel(self, 50, 30, 2, text="Filters", bg_color="green")
        lbl_conditions = CTkLabel(self, 50, 30, 2, text="Conditions", bg_color="red")
        cbx_nm = CTkCheckBox(self, width=20, height=20, border_width=4, text="Near Mint")
        cbx_sp = CTkCheckBox(self, width=20, height=20, border_width=4, text="Slightly Played")
        cbx_mp = CTkCheckBox(self, width=20, height=20, border_width=4, text="Moderately Played")        
        cbx_pd = CTkCheckBox(self, width=20, height=20, border_width=4, text="Played")        
        cbx_pr = CTkCheckBox(self, width=20, height=20, border_width=4, text="Poor")

        lbl_language = CTkLabel(self, 50, 30, 2, text="Language", bg_color="blue")
        cbx_en = CTkCheckBox(self, width=20, height=20, border_width=4, text="EN")
        cbx_fr = CTkCheckBox(self, width=20, height=20, border_width=4, text="FR")
        cbx_de = CTkCheckBox(self, width=20, height=20, border_width=4, text="DE")
        cbx_it = CTkCheckBox(self, width=20, height=20, border_width=4, text="IT")
        cbx_pt = CTkCheckBox(self, width=20, height=20, border_width=4, text="PT")
        cbx_es = CTkCheckBox(self, width=20, height=20, border_width=4, text="ES")

        lbl_extra = CTkLabel(self, 50, 30, 2, text="Extra", bg_color="yellow")      
        cbx_rev = CTkCheckBox(self, width=20, height=20, border_width=4, text="Reverse")
        cbx_sgd = CTkCheckBox(self, width=20, height=20, border_width=4, text="Signed")
        cbx_alt = CTkCheckBox(self, width=20, height=20, border_width=4, text="Altered/Misprint")
        cbx_grd = CTkCheckBox(self, width=20, height=20, border_width=4, text="Graded")
        cbx_ctz = CTkCheckBox(self, width=20, height=20, border_width=4, text="CT Zero")
        cbx_odr = CTkCheckBox(self, width=20, height=20, border_width=4, text="One Day Ready")  
        cbx_sctry = CTkCheckBox(self, width=20, height=20, border_width=4, text="Same Country")
        cbx_sctnt = CTkCheckBox(self, width=20, height=20, border_width=4, text="Same Continent")      

        # widgets rendering
        lbl_filters.pack()
        lbl_conditions.pack()
        cbx_nm.pack()
        cbx_sp.pack()    
        cbx_mp.pack()
        cbx_pd.pack()
        cbx_pr.pack()
        lbl_language.pack()
        cbx_en.pack()
        cbx_fr.pack()    
        cbx_de.pack()
        cbx_it.pack()
        cbx_pt.pack()  
        cbx_es.pack()           
        lbl_extra.pack()
        cbx_rev.pack()
        cbx_sgd.pack()    
        cbx_alt.pack()
        cbx_grd.pack()
        cbx_ctz.pack()
        cbx_odr.pack()
        cbx_sctry.pack()    
        cbx_sctnt.pack()      