
class DianYinTianTangPage:

    DT_SEARCH_LIST = "table.tbspan:nth-child({}) .ulink"

    # 搜索页test
    DT_SEARCH_INPUT = ".formhue"
    DT_SEARCH = ".searchr"
    # 搜索结果页
    DT_SEARCH_RESULT = ".ulink"
    CLOSE_NOTICE_FIXED_BOX = "#noticeFixedBox .nfbClose"
    # 资源列表
    DT_SOURCE = ("#downlist > table:nth-child({}) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a",
                 "#Zoom > table:nth-child({}) > tbody:nth-child(1) > tr:nth-child(1) > td > font")
