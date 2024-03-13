import boto3
def publish_to_sns(sub, msg):
    topic_arn = "<my sns arn>"
    sns = boto3.client("sns")
    response = sns.publish(
        TopicArn=topic_arn,
        Message=msg,
        Subject=sub
    )

def final_status(f_name, row_count, staged_row_count, status):
    sub = "Complete [{status}]: Process is complete".format(status=status)
    msg = """
        Process completed.

        ------------------------------------------------------------------------------------
        Summary of the process:
        ------------------------------------------------------------------------------------
        File Name    :   {file_name}
        Status       :   {status}
        Error        :   N/A
        Rows Read    :   {r_read}
        Rows Staged  :   {r_staged}
        ------------------------------------------------------------------------------------
        """.format(file_name=f_name, r_read=row_count, r_staged=staged_row_count, status=status)
    publish_to_sns(sub, msg)
