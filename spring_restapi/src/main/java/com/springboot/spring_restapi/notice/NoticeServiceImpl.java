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
            Integer page, Integer size,
            String order, String keyword,
            String startdate, String enddate) {
        return noticeDAO.getNoticeList(page, size, order, keyword, startdate, enddate);
    }

    @Override
    public NoticeVO getNotice(Integer id) {
        return noticeDAO.getNotice(id);

    }

    @Override
    public Integer getNoticeListCount(
            Integer page, Integer size,
            String order, String keyword,
            String startdate, String enddate) {
        return noticeDAO.getNoticeListCount(page, size, order, keyword, startdate, enddate);
    }
}
