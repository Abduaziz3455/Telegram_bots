from loader import dp
from .admins import AdminFilter
from .group_chat import IsGroup
from .private_chat import IsPrivate
from .channelfilter import IsChannel


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsChannel)
