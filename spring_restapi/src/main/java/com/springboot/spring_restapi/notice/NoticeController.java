package com.springboot.spring_restapi.notice;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.HashMap;

@RestController
@RequestMapping(path = "/api/notice")
public class NoticeController {

    @Autowired
    private NoticeServiceImpl noticeServiceImpl;

    @GetMapping(path = "/list")

    public HashMap<String, Object> getNoticeList(
            @RequestParam(value = "page") Integer page,
            @RequestParam(value = "size") Integer size,
            @RequestParam(value = "order") String order,
            @RequestParam(value = "keyword", defaultValue = "") String keyword,
            @RequestParam(value = "startdate") String startdate,
            @RequestParam(value = "enddate") String enddate) {
        List<NoticeVO> noticeList = noticeServiceImpl.getNoticeList(page, size, order, keyword, startdate, enddate);
        Integer noticeListCount = noticeServiceImpl.getNoticeListCount(page, size, order, keyword, startdate, enddate);
        HashMap<String, Object> result = new HashMap<>();
        result.put("list", noticeList);
        result.put("total", noticeListCount);

        return result;
    }

    @GetMapping(path = "/list/detail/{id}")
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