# Optimize Nextcloud

## Date

2023-05-04-Thursday.

## Environment

Ubuntu 22.04.1 LTS

## Optimize Nextcloud

```Bash
보안 및 설치 경고
이 인스턴스의 보안과 성능을 위해서 모든 것이 정확하게 설정되어야 합니다. 그러기 위해서 자동적으로 몇 가지를 확인하겠습니다. 더 자세한 정보를 위해서 링크된 문서를 참고하세요.

설정을 살펴본 결과 몇 가지 에러가 있습니다.
PHP 메모리 제한이 추천값인 512MB보다 작습니다.
"X-Robots-Tag" HTTP 헤더가 "noindex, nofollow"(으)로 설정되어 있지 않습니다. 잠재적인 정보 유출 및 보안 위협이 될 수 있으므로 설정을 변경하는 것을 추천합니다.
"X-Frame-Options" HTTP 헤더가 "SAMEORIGIN"(으)로 설정되어 있지 않습니다. 잠재적인 정보 유출 및 보안 위협이 될 수 있으므로 설정을 변경하는 것을 추천합니다.
Accessing site insecurely via HTTP. You are strongly advised to set up your server to require HTTPS instead, as described in the security tips ↗.
웹 서버에서 "/.well-known/webfinger"을(를) 올바르게 처리할 수 없습니다. 더 많은 정보를 보려면 문서 ↗를 참고하십시오.
웹 서버에서 "/.well-known/nodeinfo"을(를) 올바르게 처리할 수 없습니다. 더 많은 정보를 보려면 문서 ↗를 참고하십시오.
이메일 서버 설정이 입력되지 않았거나 검증되지 않았습니다. 기본 설정으로 이동해 설정을 완료하십시오. 서버 정보를 입력한 후 양식 아래 “이메일 발송” 버튼을 눌러 설정을 검증하십시오.
당신의 설치에서 기본 국가 번호가 설정되지 않았습니다. 프로필 설정에서 국가 번호 없이 전화번호를 사용하기 위해서 이 설정이 필요합니다. 국가 번호 없이 전화번호를 사용하게 하려면, 지역의 ISO 3166-1 코드↗를 참조하여 설정 파일에 "default_phone_region"을 추가하십시오.
매모리 캐시가 설정되지 않았습니다. 성능 향상을 위해 가능하면 memcache를 설정하십시오. 더 많은 정보는 문서 ↗를 참조하십시오.
PHP 모듈 “gmp” 혹은 “bcmath”가 활성화되지 않았습니다. WebAuthn 무암호 인증을 사용할 경우, 해당 모듈이 모두 필요합니다.
이 인스턴스의 모듈 php-imagick에 SVG 지원이 없습니다. 더 나은 호환성을 위해 설치를 권장합니다.
The "Referrer-Policy" HTTP header is not set to "no-referrer", "no-referrer-when-downgrade", "strict-origin", "strict-origin-when-cross-origin" or "same-origin". This can leak referer information. See the W3C Recommendation ↗.
설치 가이드 ↗를 다시 한 번 확인한 다음 로그의 경고나 에러를 확인하세요.

우리의 보안 검사 ↗에서 이 Nextcloud의 보안을 점검하세요.
```

### 1. Increase PHP Memory

Edit PHP Memory on `/etc/php/8.1/fpm/php.ini`:

Before:

```ini
memory_limit = 128M
```

After:

```init
memory_limit = 2048M
```

Restart PHP:

```Bash
systemctl restart php8.1-fpm
```

---

### Reference
- Optimize Nextcloud Blog KR, https://blog.dalso.org/home-server/cloudserver/300, 2023-05-04-Thu.
