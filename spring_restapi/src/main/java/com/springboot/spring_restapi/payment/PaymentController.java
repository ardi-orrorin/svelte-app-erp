package com.springboot.spring_restapi.payment;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.HashMap;

@RestController
@RequestMapping(path = "/api/payment")
public class PaymentController {

    @Autowired
    private PaymentServiceImpl paymentServiceImpl;

    @GetMapping(path = "/list")
    public HashMap<String, Object> getPaymentList(
            @RequestParam(value = "page") Integer page,
            @RequestParam(value = "size") Integer size,
            @RequestParam(value = "order") String order,
            @RequestParam(value = "keyword", defaultValue = "") String keyword,
            @RequestParam(value = "startdate") String startdate,
            @RequestParam(value = "enddate") String enddate,
            @RequestParam(value = "userid") Integer userid,
            @RequestParam(value = "authority") Integer authority) {
        List<PaymentVO> paymentList = paymentServiceImpl
                .getPaymentList(userid, authority, page, size, order, keyword,
                        startdate, enddate);
        Integer paymentListCount = paymentServiceImpl
                .getPaymentListCount(userid, authority, page, size, order, keyword,
                        startdate, enddate);

        HashMap<String, Object> result = new HashMap<>();
        result.put("list", paymentList);
        result.put("total", paymentListCount);

        return result;
    }

    @GetMapping(path = "/list/detail/{id}")
    public PaymentVO getPayment(@PathVariable Integer id) {
        PaymentVO getpayment = paymentServiceImpl.getPayment(id);
        return getpayment;
    }
}

/*
 * @RequestParam(value = "startdate") @DateTimeFormat(iso = ISO.DATE_TIME)
 * LocalDate startdate,
 * 
 * @RequestParam(value = "startdate") @DateTimeFormat(iso = ISO.DATE_TIME)
 * LocalDate enddate
 */