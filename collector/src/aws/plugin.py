import boto3

from utils.logger import get_logger


class AWSPlugin:
    def __init__(self, account_id, account_name, arn):
        self.logger = get_logger()
        self.account_id = account_id
        self.account_name = account_name
        self.arn = arn
        self.session = self.__get_session(arn)
        self.regions = self.__get_regions(self.session)

    def __get_session(self, arn: str) -> boto3.Session:
        """
        Assume the role arn from the argument and return a boto3 session.
        """
        self.logger.info(f"Assuming role: {arn}")
        sts_client = boto3.client("sts")
        assumed_role = sts_client.assume_role(
            RoleArn=arn,
            RoleSessionName="SyiCollector",
        )
        credentials = assumed_role["Credentials"]
        session = boto3.Session(
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )
        self.logger.info(f"Assumed role: {arn}")
        return session

    def __get_regions(self, session: boto3.Session) -> list[str]:
        """
        List all available AWS regions.
        :return: A list of region names.
        """
        ACTIVE_STATUSES = ["ENABLED", "ENABLED_BY_DEFAULT"]
        self.logger.info("Listing all available AWS regions.")
        regions = []
        client = session.client("account")
        paginator = client.get_paginator("list_regions")
        for page in paginator.paginate():
            regions.extend(
                [
                    region["RegionName"]
                    for region in page["Regions"]
                    if region["RegionOptStatus"] in ACTIVE_STATUSES
                ]
            )
        self.logger.info(f"Found {len(regions)} active regions.")
        return regions

    def __get_targets_data(self) -> list[dict]:
        """
        It include the EC2 instance, LBs
        """
        # Need to get ec2 data
        # Need to get LB data
        return [{}]

    def __get_dns_data(self) -> list[dict]:
        """
        It include the Route53 DNS records
        """
        return [{}]

    def get_data(self):
        pass
