package com.springboot.spring_restapi.payment;

import java.util.List;

public interface PaymentService {
        List<PaymentVO> getPaymentList(
                        Integer page, Integer size,
                        Integer userid, Integer authority,
                        String order, String keyword,
                        String startdate, String enddate);

        Integer getPaymentListCount(
                        Integer userid, Integer authority,
                        Integer page, Integer size,
                        String order, String keyword,
                        String startdate, String enddate);

        PaymentVO getPayment(Integer id);
}
