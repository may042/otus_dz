USER=$(whoami)

echo "====================="
echo "Updating package list"
sudo apt-get update
echo ""

echo "======================="
echo "Installing dependencies"
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

echo "====================="
echo "Adding Docker GPG key"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

echo "========================"
echo "Adding Docker repository"
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

echo "====================="
echo "Updating package list"
sudo apt-get update

echo "====================="
echo "Installing Docker"
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

echo "====================="
echo "Adding user to docker group"
sudo usermod -aG docker $USER
