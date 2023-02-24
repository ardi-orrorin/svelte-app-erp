package com.springboot.spring_restapi.notice;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NoticeServiceImpl implements NoticeService {

    @Autowired
    NoticeDAO noticeDAO;

    @Override
    public List<NoticeVO> getNoticeList(
            Integer skip, Integer limit,
            String order, String keyword,
            String startdate, String enddate) {
        return noticeDAO.getNoticeList(skip, limit, order, keyword, startdate, enddate);
    }

    @Override
    public NoticeVO getNotice(Integer id) {
        return noticeDAO.getNotice(id);
    }

}
