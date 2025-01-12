#pip install alpaca-trade-api

import os
from alpaca_trade_api import REST, TimeFrame
import pandas as pd


class trading():

    def __init__(self):
        # Récupérer les clés API depuis les variables d'environnement
        self.API_KEY = os.getenv('APCA_API_KEY_ID')
        self.API_SECRET = os.getenv('APCA_API_SECRET_KEY')
        self.BASE_URL = 'https://paper-api.alpaca.markets'  # Utiliser l'URL pour le paper trading
        
        # Initialiser l'API REST d'Alpaca
        self.api = REST(self.API_KEY, self.API_SECRET, self.BASE_URL, api_version='v2')
        
        # Vérifier la connexion
        account = self.api.get_account()
        if account.status != 'ACTIVE':
            raise Exception('Compte Alpaca non actif. Vérifiez vos clés API et l\'URL.')

    def open_order(self, ticker_buy, ticker_sell, qty_buy, qty_sell, type_order='market', time_in_force='gtc'):
        try:
            # Placer l'ordre d'achat
            ordre_buy = self.api.submit_order(
                symbol=ticker_buy,
                qty=qty_buy,
                side='buy',
                type=type_order,
                time_in_force=time_in_force
            )
            
            # Placer l'ordre de vente
            ordre_sell = self.api.submit_order(
                symbol=ticker_sell,
                qty=qty_sell,
                side='sell',
                type=type_order,
                time_in_force=time_in_force
            )
            
            return ordre_buy, ordre_sell
        except Exception as e:
            raise Exception(f"Erreur lors du placement des ordres de paire: {e}")
    
    def close_order(self, ticker_buy, ticker_sell, type_order='market', time_in_force='gtc'):
        try:
            # Récupérer les positions actuelles
            position_buy = self.api.get_position(ticker_buy)
            position_sell = self.api.get_position(ticker_sell)
            
            # Placer l'ordre de vente pour l'actif acheté
            ordre_close_buy = self.api.submit_order(
                symbol=ticker_buy,
                qty=position_buy.qty,
                side='sell',
                type=type_order,
                time_in_force=time_in_force
            )
            
            # Placer l'ordre d'achat pour l'actif vendu
            ordre_close_sell = self.api.submit_order(
                symbol=ticker_sell,
                qty=position_sell.qty,
                side='buy',
                type=type_order,
                time_in_force=time_in_force
            )
            
            return ordre_close_buy, ordre_close_sell
        except Exception as e:
            raise Exception(f"Erreur lors de la fermeture des positions de paire: {e}")