package com.springboot.spring_restapi.payment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PaymentServiceImpl implements PaymentService {

    @Autowired
    PaymentDAO paymentDAO;

    @Override
    public List<PaymentVO> getPaymentList(
            Integer userid, Integer authority,
            Integer page, Integer size,
            String order, String keyword,
            String startdate, String enddate) {
        return paymentDAO.getPaymentList(userid, authority, page,
                size, order, keyword, startdate, enddate);
    }

    @Override
    public PaymentVO getPayment(Integer id) {
        return paymentDAO.getPayment(id);
    }

    @Override
    public Integer getPaymentListCount(
            Integer userid, Integer authority,
            Integer page, Integer size,
            String order, String keyword,
            String startdate, String enddate) {
        return paymentDAO.getPaymentListCount(userid, authority, page, size,
                order, keyword, startdate, enddate);
    }
}
