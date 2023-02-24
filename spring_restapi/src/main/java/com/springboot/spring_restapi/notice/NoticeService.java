package com.springboot.spring_restapi.notice;

import java.util.List;

public interface NoticeService {
    List<NoticeVO> getNoticeList(
            Integer skip, Integer limit,
            String order, String keyword,
            String startdate, String enddate);

    NoticeVO getNotice(Integer id);
}
