from enum import Enum

class BearerToken(Enum):
    TOKEN = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJjYXJkdHJhZGVyLXByb2R1Y3Rpb24iLCJzdWIiOiJhcHA6OTc5MyIsImF1ZCI6ImFwcDo5NzkzIiwiZXhwIjo0ODcyMzA2MzQyLCJqdGkiOiI4NDk2Zjg5NS02NjIxLTQ5MjYtYjI1Yi03ZjU4M2VmZWFlNGUiLCJpYXQiOjE3MTY2MzI3NDIsIm5hbWUiOiJUaW5hcmkgQXBwIDIwMjQwNDAzMjIxNTUwIn0.uhmNYPsThK4xuV2l7SVCyFd4QRpJ-DkiSc2uPQjkfAyb8JuCJjJh2NXuGudbimkb_lCYPwJzpFL01ZCDnCTy71LwHHT4Y3CKGVpVdX3jGo-2Oym_kwTBJGrD8GegHgXxhcuYFPsPQptnu9oUTkeByLw5XGdTIGiVvwm4mCGbvtn-WKnefj81YFP9UOOuishcSw2X5sS79eID_bKKsKZH1J73e4pT4NeUon5piJsTt9elcrookzJXbXNRIgNobmuf9Yx5-LFQHgTM3mVXp9acrclGkmmvS3rGWtXkocM4vCcbU8_RGN_20t8MCqhFKplMeXAW6raik_c1b5NTnusH5Q"

class GamesApi(Enum):
    GET_ALL_GAMES = "https://api.cardtrader.com/api/v2/games"
    GET_ALL_EXPANSIONS = "https://api.cardtrader.com/api/v2/expansions"
    GET_LISTING_BY_EXPANSION_ID  = "https://api.cardtrader.com/api/v2/marketplace/products?expansion_id="

class CartApi(Enum):
    ADD_PRODUCT_TO_CART = "https://api.cardtrader.com/api/v2/cart/add"
    