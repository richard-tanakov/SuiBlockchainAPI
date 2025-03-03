import json
import logging
from sqlmodel import create_engine, Field, SQLModel, Session, select, update, insert

import os
from dotenv import load_dotenv

from datetime import datetime


logging.basicConfig(level=logging.INFO, filename="Getlog.log", filemode="a")
load_dotenv()
link = os.getenv("engine_link")
engine = create_engine(link, echo=True)


""" Date manipulation """


def dateСonversion(createTimestamp):
    createTimestamp = datetime.fromtimestamp(createTimestamp / 1e3)
    return str(createTimestamp)


def statusСheck(status, data, inquiryInformation, coin):
    """Checking the status of a request"""

    match status:
        case 200:

            return json.loads(data)
            
        case _:
            pass


class Token(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    coinType: str | None = Field(default=None)
    objectId: str | None = Field(default=None)
    coinName: str | None = Field(default=None)
    coinDenom: str | None = Field(default=None)
    decimals: int | None = Field(default=None)
    coinSymbol: str | None = Field(default=None)
    imgUrl: str | None = Field(default=None)
    description: str | None = Field(default=None)
    supply: float | None = Field(default=None)
    supplyInUsd: float | None = Field(default=None)
    price: float | None = Field(default=None)
    fdv: float | None = Field(default=None)
    holdersCount: int | None = Field(default=None)
    packageId: str | None = Field(default=None)
    creatorAddress: str | None = Field(default=None)
    creatorName: str | None = Field(default=None)
    creatorImg: str | None = Field(default=None)
    createTimestamp: datetime | None = Field(default=None)
    isVerified: bool | None = Field(default=None)
    isBridged: bool | None = Field(default=None)
    socialDiscord: str | None = Field(default=None)
    socialEmail: str | None = Field(default=None)
    socialGitHub: str | None = Field(default=None)
    socialTelegram: str | None = Field(default=None)
    socialTwitter: str | None = Field(default=None)
    securityMessage: str | None = Field(default=None)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime | None = Field(default=None)

    SQLModel.metadata.create_all(engine)


class Holders(SQLModel, table=True):
    """Top wallets by coinClick to apply"""

    id: int | None = Field(default=None, primary_key=True)
    holderAddress: str
    holderName: str | None = Field(default=None)
    holderImg: str | None = Field(default=None)
    coinType: str | None = Field(default=None)
    coinDenom: str | None = Field(default=None)
    holderSecurityMessage: str | None = Field(default=None)
    amount: float | None = Field(default=None)
    usdAmount: float | None = Field(default=None)
    percentage: float | None = Field(default=None)
    objectsCount: int | None = Field(default=None)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    SQLModel.metadata.create_all(engine)


""" Bulk data to update or overwrite in the database  """


def dataPackagingOfСoins(dataGetToken, metaDataToken):

    tokens = {
        "coinType": (dataGetToken["coinType"]),
        "objectId": (dataGetToken["objectId"]),
        "coinName": (dataGetToken["coinName"]),
        "coinDenom": (dataGetToken["coinDenom"]),
        "decimals": dataGetToken["decimals"],
        "coinSymbol": dataGetToken["coinSymbol"],
        "imgUrl": dataGetToken["imgUrl"],
        "description": dataGetToken["description"],
        "supply": dataGetToken["supply"],
        "supplyInUsd": dataGetToken["supplyInUsd"],
        "price": dataGetToken["price"],
        "fdv": dataGetToken["fdv"],
        "holdersCount": dataGetToken["holdersCount"],
        "packageId": dataGetToken["packageId"],
        "creatorAddress": dataGetToken["creatorAddress"],
        "creatorName": dataGetToken["creatorName"],
        "creatorImg": dataGetToken["creatorImg"],
        "createTimestamp": dateСonversion(dataGetToken["createTimestamp"]),
        "isVerified": dataGetToken["isVerified"],
        "isBridged": dataGetToken["isBridged"],
        "socialDiscord": metaDataToken["socialDiscord"],
        "socialEmail": metaDataToken["socialEmail"],
        "socialGitHub": metaDataToken["socialGitHub"],
        "socialTelegram": metaDataToken["socialTelegram"],
        "socialTwitter": metaDataToken["socialTwitter"],
        "securityMessage": metaDataToken["securityMessage"],
        "updated_at": datetime.now(),
    }

    with Session(engine) as session:
        getTok = (
            session.query(Token)
            .filter(Token.coinType == tokens["coinType"])
            .update(tokens)
        )
        session.commit()
        if not getTok:

            token = insert(Token).values(tokens)
            session.execute(token)
            session.commit()
        session.close()

def dataPackagingOfHolders(holder):

    holder = {
        "holderAddress": str(holder["holderAddress"]),
        "holderName": str(holder["holderName"]),
        "holderImg": str(holder["holderImg"]),
        "coinType": str(holder["coinType"]),
        "coinDenom": str(holder["coinDenom"]),
        "holderSecurityMessage": str(holder["holderSecurityMessage"]),
        "amount": float(holder["amount"]),
        "usdAmount": float(holder["usdAmount"]),
        "percentage": float(holder["percentage"]),
        "objectsCount": int(holder["objectsCount"]),
        "updated_at": datetime.now(),
    }

    with Session(engine) as session:
        getHolder = (
            session.query(Holders)
            .filter(Holders.holderAddress == holder["holderAddress"])
            .update(holder)
        )
        session.commit()
        if not getHolder:

            holders = insert(Holders).values(holder)
            session.execute(holders)
            session.commit()
        session.close()