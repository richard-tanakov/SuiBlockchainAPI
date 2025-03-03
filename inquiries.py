import requests
import time
import DataHandling

def getApiToken(coin, headers):
        """ Application for basic data for coins """
        url = f"https://api.blockberry.one/sui/v1/coins?page=0&size=50&orderBy=DESC&sortBy=NAME&searchStr={coin}"
        time.sleep(15)
        response = requests.get(url, headers=headers)
        data = response.text
        inquiryInformation = f'The {coin} request caused an error'
        status = response.status_code 
        return(DataHandling.statusСheck(status,data,inquiryInformation,coin))

def getApiMetaDataToken(coin, headers):
        """ Takes out the coin contacts """

        url = f"https://api.blockberry.one/sui/v1/coins/metadata/{coin}"
        time.sleep(15)
        response = requests.get(url, headers=headers)
        data = response.text
        inquiryInformation = f'{coin} metadata request ended with an error'
        status = response.status_code 
        return(DataHandling.statusСheck(status,data,inquiryInformation,coin))


def getApiTopHoldersCoin(coin, headers ):
        """ Obtaining top purse holders (whales) """
        
        url = f"https://api.blockberry.one/sui/v1/coins/{coin}/holders?page=0&size=20&orderBy=DESC&sortBy=AMOUNT"

        time.sleep(15)
        response = requests.get(url=url, headers=headers)
        data = response.text
        inquiryInformation = f'request for top wallets caused an error with the {coin}.'
        status = response.status_code 
        return(DataHandling.statusСheck(status,data,inquiryInformation,coin))
        

def getDexStatistics(headers):
        url = "https://api.blockberry.one/sui/v1/dex?page=0&size=50&orderBy=DESC&period=MONTH&sortBy=CURRENT_TVL"
        time.sleep(15)
        response = requests.get(url=url, headers=headers)
        data = response.text
        inquiryInformation = f'dex query failed'
        status = response.status_code 
        return(DataHandling.statusСheck(status,data,inquiryInformation))

        





        


