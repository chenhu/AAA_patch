REM INSERTING into M_FUNCTION_URL_FILTER
SET DEFINE OFF;
Insert into M_FUNCTION_URL_FILTER (FUNCID,SYSTEMID,MATCHTYPE,URLPATTERN,MATCHRESULT,PRIORITY,DESCRIPTION) values ('006003001',1,0,'/fixedline/online/enterpriseuser/massquery.jsp',null,0,'jsp filter');
Insert into M_FUNCTION_URL_FILTER (FUNCID,SYSTEMID,MATCHTYPE,URLPATTERN,MATCHRESULT,PRIORITY,DESCRIPTION) values ('006003001',1,0,'/fixedline/online/enterpriseuser/query_show.action',null,0,'action filter');
