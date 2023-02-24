package com.springboot.spring_restapi.notice;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import java.time.LocalDateTime;

@RestController
@RequestMapping(path = "/notice")
public class NoticeController {

    @Autowired
    private NoticeServiceImpl noticeServiceImpl;

    @GetMapping(path = "/list")
    public List<NoticeVO> getNoticeList(
            @RequestParam(value = "skip") Integer skip,
            @RequestParam(value = "limit") Integer limit,
            @RequestParam(value = "order") String order,
            @RequestParam(value = "keyword", defaultValue = "") String keyword,
            @RequestParam(value = "startdate") String startdate,
            @RequestParam(value = "enddate") String enddate) {
        List<NoticeVO> noticeList = noticeServiceImpl.getNoticeList(skip, limit, order, keyword, startdate, enddate);
        return noticeList;
    }

    @GetMapping(path = "/detail/{id}")
    public NoticeVO getNotice(@PathVariable Integer id) {
        NoticeVO getnotice = noticeServiceImpl.getNotice(id);
        return getnotice;
    }
}

/*
 * @RequestParam(value = "startdate") @DateTimeFormat(iso = ISO.DATE_TIME)
 * LocalDate startdate,
 * 
 * @RequestParam(value = "startdate") @DateTimeFormat(iso = ISO.DATE_TIME)
 * LocalDate enddate
 */