from log_helper_class import PutLog


def my_tes():
    PutLog.info("info mess mnn")
    print("info mess")
    PutLog.error("error log 124")
    PutLog.warn("warm log 897")
    return {}

my_tes()