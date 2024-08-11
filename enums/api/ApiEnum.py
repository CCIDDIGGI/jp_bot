from enum import Enum

class InfoApi(Enum):
    GET_INFO = "https://api.cardtrader.com/api/v2/info"

class GamesApi(Enum):
    GET_ALL_GAMES = "https://api.cardtrader.com/api/v2/games"
    GET_ALL_EXPANSIONS = "https://api.cardtrader.com/api/v2/expansions"
    GET_LISTING_BY_EXPANSION_ID  = "https://api.cardtrader.com/api/v2/marketplace/products?expansion_id="

class CartApi(Enum):
    ADD_PRODUCT_TO_CART = "https://api.cardtrader.com/api/v2/cart/add"
    