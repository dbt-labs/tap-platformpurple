from .events import EventsStream
from .transactions import TransactionsStream
from .products import ProductsStream
from .user_access import UserAccessStream
from .user_info import UserInfoStream
from .user_referrals import UserReferralsStream


AVAILABLE_STREAMS = [
    EventsStream,
    TransactionsStream,
    ProductsStream,
    UserAccessStream,
    UserInfoStream,
    UserReferralsStream,
]
