#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests
import argparse


class Whiteout Survival:
    def __init__(self):
        self.ua = "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"

    @staticmethod
    def __user_data():
        user_data = ['GUEST-XXXXXXXXX', 'GUEST-XXXXXXXXX']
        return user_data

    @staticmethod
    def __get_result(ret):
        if ret == "RESPONSE_CODE_SUCCESS":
            return "상품이 정상적으로 지급되었습니다."
        elif ret == "RESPONSE_CODE_ACCOUNT_NOT_FOUND":
            return "DevPlay 계정을 다시 한번 확인해주세요."
        elif ret == "RESPONSE_CODE_COUPON_CODE_NOT_FOUND":
            return "쿠폰번호를 다시 한번 확인해주세요."
        elif ret == "RESPONSE_CODE_NOT_TARGET_COUNTRY":
            return "유효하지 않은 쿠폰 코드입니다."
        elif ret == "RESPONSE_CODE_NOT_EVENT_TIME":
            return "쿠폰 사용기간이 아닙니다. 유효기간을 다시 한번 확인해 주세요."
        elif ret == "RESPONSE_CODE_COUPON_CODE_ALREADY_USED":
            return "이미 사용된 쿠폰입니다."
        elif ret == "RESPONSE_CODE_COUPON_USAGE_ALREADY_MAX":
            return "사용할 수 있는 쿠폰 수를 초과하였습니다."
        else:
            return "서버에서 알 수 없는 응답이 발생하였습니다. 잠시후 다시 시도해주세요."

    def __post_coupon(self, post_data):
        url = 'https://wos-giftcode.centurygame.com/'
        headers = {'Content-Type': 'application/json', 'User-Agent': self.ua}
        try:
            r = requests.post(url=url, headers=headers, json=post_data)
            if r.status_code != 200:
                return self.__get_result(1)
            else:
                obj = json.loads(r.text)
                return self.__get_result(obj.get('responseCode'))
        except Exception as err:
            print("post_coupon:: {err}".format(err=err))

    def registration_coupon(self, coupon_data):
        for user in self.__user_data():
            post_data = {
                "email": user,
                "game_codeL": "ck",
                "coupon_code": coupon_data
            }
            print("{user} :: {result}".format(user=user, result=self.__post_coupon(post_data)))
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='WhiteoutSurvival Coupon', description='WOS 쿠폰 등록')
    try:
        parser.add_argument('-c', '--coupon', dest='coupon_code', type=str, help='WOS 쿠폰 번호')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')
        args = parser.parse_args()
        crk = WhiteoutSurvival()
        if args:
            crk.registration_coupon(args.coupon_code)
            sys.exit(0)
    except Exception as err:
        print("main:: {err}".format(err=err))
        sys.exit(0)
