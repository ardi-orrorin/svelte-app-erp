package com.springboot.spring_restapi.payment;

import java.time.LocalDateTime;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class PaymentVO {
    private Integer id;
    private String corp_name;
    private String bank_name;
    private String bank_account;
    private String bank_number;
    private Integer money;
    private String memo;
    private LocalDateTime create_date;
    private String name;

}
