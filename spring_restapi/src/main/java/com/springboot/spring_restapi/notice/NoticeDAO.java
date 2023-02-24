package com.springboot.spring_restapi.notice;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface NoticeDAO {

    List<NoticeVO> getNoticeList(
            @Param("page") Integer page, @Param("size") Integer size,
            @Param("order") String order, @Param("keyword") String keyword,
            @Param("startdate") String startdate, @Param("enddate") String enddate);

    Integer getNoticeListCount(
            @Param("page") Integer page, @Param("size") Integer size,
            @Param("order") String order, @Param("keyword") String keyword,
            @Param("startdate") String startdate, @Param("enddate") String enddate);

    NoticeVO getNotice(Integer Id);
}
