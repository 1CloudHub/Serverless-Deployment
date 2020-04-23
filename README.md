# Serverless-Deployment

AWS CloudFormation template creates the following resources in AWS account.

- Amazon S3 bucket to store the raw data
- Glue Connection to connect source database
- Glue Crawler and Glue Jobs
- IAM roles for accessing AWS Glue and Amazon S3


#### Deployment Steps:
1.	Login into your AWS Account.
2.	Navigate to **CloudFormation** and create new stack.
3.	In Specify **template**, Upload the template file.

![template]( https://github.com/1CloudHub/Azure-AKS/blob/master/AWS%20Images/capture-1.png )


4.	On the **Specify Details** page, Enter Stack name. Review the parameters of the template and provide the required values.

**Parameters & Values**

|  Parameter Name | Default   | Description  |
| ------------------- | ---------- | ------------- |
|  RawBucket | Requires Input  | Name of the Bucket to Store the Raw data. Note: Provide Unique name for S3 bucket|
|  ScriptBucketName | Requires Input  | Name of the S3 bucket name, where script has been uploaded.   |
|  ConnectionName |  Requires Input | Glue Connection Name  |
| GlueAZ  | ap-south-1a   | Must be AWS Availbility Zone for Glue Connection   |
|SecurityGroupID | Requires Input | Security Group ID for Glue Connection. Security group created in VPC and correct region.|
|Subnet|Requires Input | Subnet ID for Glue Connection. Must be Private Subnet. |
|JDBCString | Requires Input | Database Connection String. Connection URL. |
|DBUser | Requires Input | Username for the source DB |
|DBPassword | Requires Input  |Password for the source DB.  |
|DBName | Requires Input |  Source DB Name  |
|TableName  | Requires Input  | Source Table Name |
|PartitionKeys  | Requires Input  | Column names for the partitions separated by comma (eg.'column1,column2') |
|CrawlerSchedule  | cron(30 0 * * ? * ) | Crawler Execution Schedule Cron Expression. Default is daily at 12:30 AM GMT  |
|LakeDBName | Requires Input  | Name to be used in analytical tools such as Athena and Redshift to reference these tables within the data lake.|


5.	On the **Options page**, you can specify tags (key-value pairs) for resources in stack and Click on Next.
6.	On the **Review page**, review and confirm the template settings. Under Capabilities, select the **check box to acknowledge** that the template will create IAM resources.

![Checkbox]( https://github.com/1CloudHub/Azure-AKS/blob/master/AWS%20Images/capture-2.png )

7.	Click on **Create** to deploy the stack

#### **Conclusion**

We have provided an AWS CloudFormation template which allows you to quickly setup the DataLake resources and analysis your data in Analytical tools.


###End
