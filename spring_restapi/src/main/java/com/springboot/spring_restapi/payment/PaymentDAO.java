package com.springboot.spring_restapi.payment;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface PaymentDAO {

        List<PaymentVO> getPaymentList(
                        @Param("userid") Integer userid, @Param("authority") Integer authority,
                        @Param("page") Integer page, @Param("size") Integer size,
                        @Param("order") String order, @Param("keyword") String keyword,
                        @Param("startdate") String startdate, @Param("enddate") String enddate);

        Integer getPaymentListCount(
                        @Param("userid") Integer userid, @Param("authority") Integer authority,
                        @Param("page") Integer page, @Param("size") Integer size,
                        @Param("order") String order, @Param("keyword") String keyword,
                        @Param("startdate") String startdate, @Param("enddate") String enddate);

        PaymentVO getPayment(Integer Id);
}
