package com.springboot.spring_restapi.notice;

import java.time.LocalDateTime;

import jakarta.validation.constraints.Size;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class NoticeVO {

    private Integer id;

    @Size(max = 100)
    private String title;

    private String body;

    private Integer pin;

    private Integer user_id;

    private LocalDateTime create_date;

}
