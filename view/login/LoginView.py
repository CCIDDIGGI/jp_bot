from customtkinter import *
import requests

class LoginView:    
    
    def __init__(self) -> None:
        pass 


    def greet_event(self):
        print("CLICKED")
        print(self.get_info("https://api.cardtrader.com/api/v2/info", "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJjYXJkdHJhZGVyLXByb2R1Y3Rpb24iLCJzdWIiOiJhcHA6OTc5MyIsImF1ZCI6ImFwcDo5NzkzIiwiZXhwIjo0ODcxOTA1MjYxLCJqdGkiOiIwMTdjNDZiOC05NmQ1LTQ0NzMtYTA3OC02YzEyY2Q1MDA2MjMiLCJpYXQiOjE3MTYyMzE2NjEsIm5hbWUiOiJUaW5hcmkgQXBwIDIwMjQwNDAzMjIxNTUwIn0.u_QsTlQErxV6LWrD0y2r5AMNoTds5qxTT2QaHVNwO_BxxS3mwEMwAg-muMOGJc6VuXb9UOBqTtdZdgmxHO65GV9NNn0xFbTgtZUTkHMrpNPXFeYXA8SxSv3jXOfg4agrC_aO5DekGJ2qoHJuXwaqdzbNln39wJmfsOnMVwVrmq5nbNjgn5LI6CEFk2Ri4sAe01dyYTGk0xPlbr_m63rrl5ridcFSlE3H2LXfkocbnXoLDEqgd9Z6HjAtqGTnd15PrQeTgBevvarrdnrQAtbt-eaXHMtQM2HJ6OgG8Q-6Jc3yU2P3A29Hs2YsqO-d8ZsEqIIPGQg1MurvtKt7CtMjeQ"))


    def init_view(self):

        app = CTk()
        app.geometry("500x400") 

        btn = CTkButton(app, text="Prova!", command=self.greet_event)
        btn.place(relx=0.5, rely=0.5, anchor="center")

        app.mainloop()
    
    def get_info(self, url, token):

        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:   
            return response.status_code, response.text