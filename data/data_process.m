LAll = load('./LAll/mirflickr25k-lall.mat');
YAll = load('./YAll/mirflickr25k-yall.mat');
images = load('./IAll/mirflickr25k-iall.mat');
save('FLICKR-25K.mat','images','LAll','YAll','-v7.3')
