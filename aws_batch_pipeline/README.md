## Flow
![image](https://github.com/youngmin-jin/practice/assets/135728064/dc5f0e15-f5cd-45da-b0ed-00d1b9fb2f6f)


## Steps
1. Data Exchangeから取得したローデータをS3に格納する
2. Glue Crawlerを使用して、S3にあるローデータをGlue DataCatalogに格納する
3. ETL jobを使用して、ローデータを前処理し、S3に格納するPythonジョブファイルを作成する
4. Glue Crawlerを使用して、S3にある前処理されたデータをGlue DataCatalogに格納する
5. Athenaでデータを確認する
