</path/to/saved/keypair/file.pem>
/Users/yasha.podeswa/.ssh/aws-personal-uswest-oregon.pem

<master.public-dns-name.amazonaws.com>
ec2-54-191-166-139.us-west-2.compute.amazonaws.com

# Connecting to Hadoop
ssh -o "ServerAliveInterval 10" -i ~/.ssh/aws-personal-uswest-oregon.pem hadoop@ec2-54-191-166-139.us-west-2.compute.amazonaws.com

# Monitoring Hadoop jobs
ssh -L 9100:localhost:9100 -L 9101:localhost:9101  -i ~/.ssh/aws-personal-uswest-oregon.pem hadoop@ec2-54-191-166-139.us-west-2.compute.amazonaws.com
# Then open in browser:
http://localhost:9101