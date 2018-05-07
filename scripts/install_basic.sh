#!/bin/bash

echo "=================== Setup deployer user ==================="

deployer_user=deployer
deployer_group=${deployer_user}

ssh_dir=/home/${deployer_user}/.ssh
authorized_keys=${ssh_dir}/authorized_keys

# Create user
if grep -q ${deployer_user} /etc/passwd; then
  echo "user ${deployer_user} is exists"
else
  useradd ${deployer_user}
fi

# Create sudoers
cat << EOF > /etc/sudoers.d/${deployer_group}
%${deployer_group} ALL=(ALL:ALL) ALL
EOF

# Key based authentication
mkdir -p ${ssh_dir} && chmod 700 ${ssh_dir} \
&& touch ${authorized_keys}

cat << EOF > ${authorized_keys}
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDASFZm2l+I+1HNhTUyFdP30RNa76RhxrQgiYe21oZ1vw/nblmHdBnNAjMMIwJjIkhnVeLh6VeNrUekQVySgT/grijNix0myQ7qKFPM+ucDziMO1dCUSMALSDlF2zKPun40YwPvv9z4HV7PoUaH/PigzKXO2I88rWp+bdFBLiArinC3l+PkOg8BjTVzAgt+8tp932z16tLB9cYy/zFRE6/PGQLl2Uj3H6DQ+j1TyrEtZsJMoV/fTlCO8Vcn1sClDJwkhTxtRXFEbR82JsPsGNdG8BiUf0l+lbFgZEXts9fVMKKOQDHPsfhSSJmTa0xW+no+vsMCnVXwUjjxqnuJjZc7 manhdung@manhdungs-MacBook-Air.local
EOF

chmod 600 ${authorized_keys} && chown -R ${deployer_user}:${deployer_user} ${ssh_dir}

# Set passwd
passwd ${deployer_user}

# Update
yum update -y
