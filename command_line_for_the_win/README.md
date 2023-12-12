# Project Title: Command line for the win

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

I have learned About SFTP

challenge is found at [here](https://cmdchallenge.com)

## Usage

1. Open a terminal or command prompt on your local machine.
2. Use the following command to connect to your remote sandbox via SFTP:
     -sftp username@remote_sandbox_ip

Replace username with your actual username and remote_sandbox_ip with the IP address or hostname of your remote sandbox. You'll be prompted to enter your password.
3.Once connected, navigate to the directory on your local machine where the images are located using the lcd (local change directory) command. For example:
      - lcd /path/to/local/images

4. Navigate to the directory on the remote sandbox where you want to upload the images using the cd (change directory) command. For example:

   	- cd /path/to/remote/upload/directory
5. Use the put command to upload the images. For example:
       - put image1.jpg image2.png

6. finaly exit