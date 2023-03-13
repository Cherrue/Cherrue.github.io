---
layout: single
title: \[기술블로그\] 3월 2주 주간 기술블로그 Follow Up
date: 2023-03-13 01:44:11 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2023-03-06 ~ 2023-03-13 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

## [뭐 이런 것도 다 픽업 됩니다!(배민스토어 픽업 플랫폼 및 셀러서비스편)](https://techblog.woowahan.com/10593/)

 배민스토어 픽업서비스는 어떤 가치를 실현하고자 하였을까요

 있으시다면 배민스토어 픽업은 어떤 가치가 있었나요

 셀러는 배민스토어에 쉽게 입점하여 픽업서비스를 제공할 수 있어야 하고

---



# [kakao Tech](https://tech.kakao.com/feed/)

---



# [WATCHA 팀 블로그](https://medium.com/feed/watcha)

---



# [무신사 기술 블로그](https://medium.com/feed/musinsa-tech)

---



# [야놀자](https://medium.com/feed/yanolja)

---



# [직방 TECH](https://medium.com/feed/zigbang)

---



# [Google Developers](https://developers.googleblog.com/feeds/posts/default?alt=rss)

## [How to be more productive as a developer: 5 app integrations for Google Chat that can help](http://developers.googleblog.com/2023/03/how-to-be-more-productive-as-developer-5-app-integrations-for-google-chat-that-can-help.html)

 With Asana for Google Chat you can easily create tasks get notifications update tasks assign them to the right people and track your progress

 How to Use Jira for Google Chat Jenkins Jenkins allows you to automate your builds and deployments

 How to Use Jenkins for Google Chat GitHubGitHub lets you manage your code and collaborate with your team

## [#WeArePlay | Meet Ania from Canada. More stories from USA, Australia and Montenegro](http://developers.googleblog.com/2023/03/weareplay-meet-ania-from-canada-more-stories-from-usa-australia-and-montenegro.html)

 Posted by Leticia Lago Developer Marketing   This International Womens Day were dedicating our latest WeArePlay stories to the inspirational women founders creating apps and games businesses on Google Play

 Realizing there wasnt much help readily available on mobile she took it upon herself to do her own research and learn how to manage her anxiety

 After feeling more confident again she wanted to share what she had learned and help people so began developing Rootd

## [Let’s go. It’s Google I/O 2023](http://developers.googleblog.com/2023/03/lets-go-its-google-io-2023.html)

 Posted by Jeanine Banks VP  General Manager Developer X and Head of Developer Relations     Google IO is back and youre invited to join us online May 10

 Youll also get to hear about ways to use the latest in technology from AI and cloud to mobile and web

 We look forward to seeing you in May

---



# [Amazon Science Blog](https://www.amazon.science/index.rss)

---



# [THE NETFLIX TECH BLOG](https://netflixtechblog.com/feed)

## [Elasticsearch Indexing Strategy in Asset Management Platform (AMP)](https://netflixtechblog.com/elasticsearch-indexing-strategy-in-asset-management-platform-amp-99332231e541?source=rss----2615bd06b42e---4)

 We have a schema management microservice which is used to store the taxonomy of each asset type and this programmatically created new indices whenever new asset types were created in this service

 All the assets of a specific type use the specific index defined for that asset type to create or update the asset document

 We created an index template in Elasticsearch so that the new indices always use the same settings and mappings stored in the template

## [Data Reprocessing Pipeline in Asset Management Platform @Netflix](https://netflixtechblog.com/data-reprocessing-pipeline-in-asset-management-platform-netflix-46fe225c35c9?source=rss----2615bd06b42e---4)

 Hence we built the data pipeline that can be used to extract the existing assets metadata and process it specifically to each new use case

 We build the data pipeline to persist the assets data in the iceberg in parallel with cassandra and elasticsearch DB

 We have set up the different clusters of data extractor and processor from the main Production cluster to process the older assets data to avoid any impact of the assets operations live in production

## [NTS: Reliable Device Testing at Scale](https://netflixtechblog.com/nts-reliable-device-testing-at-scale-43139ae05382?source=rss----2615bd06b42e---4)

 However NTS is built around the use case where users come in with a specific resource or pool of similar resources in mind and are searching for a subset of compatible tests to run on the target resources

 This contrasts with test automation systems where users come in with a set of diverse tests and are searching for compatible resources on which to run the tests

 However the batch execution service maintains its own data model of the test execution that is separate from and thus incompatible with that materialized by the test dispatcher service

## [Data ingestion pipeline with Operation Management](https://netflixtechblog.com/data-ingestion-pipeline-with-operation-management-3c5c638740a8?source=rss----2615bd06b42e---4)

 We use Cassandra as a source of truth where we store the annotations while we index annotations in ElasticSearch to provide rich search functionalities

 StartAnnotationOperationWhen this API is called we store the operation with its OperationKey tuple of annotationType annotationType Version and pivotId in our database

 StartAnnotationOperationUpsertAnnotationsInOperationUsers call this API to upsert the annotations in an Operation

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

## [Reducing Apache Spark Application Dependencies Upload by 99%](https://engineering.linkedin.com/blog/2023/reducing-apache-spark-application-dependencies-upload-by-99-)

 A dependency cache can be created to store commonly used dependencies and eliminate the need for repetitive uploading

 Based on our observations and analysis we decided to implement the dependency cache at user level

 We gradually ramped this feature up within clusters and across clusters to minimize the risk of major failure caused by this feature

## [AI @ LinkedIn - It’s All About Foundations](https://engineering.linkedin.com/blog/2023/aI-at-linkedin-it-is-all-about-foundations)

 This guides us in the tools and technologies we build with a focus on delivering value to our members and customers

 When we bring together generative AI with datasets like our Economic Graph thats where we can get even better at helping professionals connect to opportunities showcase their skills and gain the knowledge they need to be better at their job and in their career

 Almost 20 years ago this company was founded with a clear vision  create economic opportunity for every member of the global workforce  and well continue to use AI responsibly to help us accelerate our progress toward that vision

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

## [Introducing Velox: An open source unified execution engine](https://engineering.fb.com/2023/03/09/open-source/velox-open-source-execution-engine/)

 Velox helps consolidate and unify data management systems in a manner we believe will be of benefit to the industry

 Velox unifies the common dataintensive components of data computation engines while still being extensible and adaptable to different computation engines

 IO a set of APIs that allows Velox to be integrated in the context of other engines and runtimes such as

---



# [slack engineering](https://slack.engineering/feed/)

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
