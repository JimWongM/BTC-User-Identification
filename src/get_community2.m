function [lables center]= get_community2(data, centers , num_clusters)

% This function is modified from:
%   http://scgroup.hpclab.ceid.upatras.gr/scgroup/Projects/TMG/
% weight location
% attri 0 1 vote problem

nn=2708;
ff=1433;
d=1433;

timi=18

iter = 0;
qold = inf;
threshold = 0.001;
data= data';   
centers = double(centers);
load('cora.mat');

%
% Calculate the distance (square) between data and centers
%
n = size(data, 1);
x = sum(data.*data, 2)';
X = repmat(x, num_clusters, 1);
y = sum(centers.*centers, 2);
Y = repmat(y, 1, n);
% data->nf have taken weight in
P = X + Y - 2*centers*data'; % c*n


[~, ind] = min(P, [], 1);
lables = ind';
center= centers;
q=0;

weight=eye(d);
nweight=diag(weight)';
% add adaptive weight
while 1
  iter = iter + 1;
  disp('iter:');
  disp(iter);
  [val, ind] = min(P, [], 1); % ind 1*6339
  %disp(ind);
  P = sparse(ind, 1:n, 1, num_clusters, n);
  centers = P*data;
  cluster_size = P*ones(n, 1);
  zero_cluster = find(cluster_size==0);
 
  
  
  if length(zero_cluster) > 0
    rnd_Idx = randperm(size(data,1),length(zero_cluster));  
    init_centers= data(rnd_Idx,:); 
    cluster_size(zero_cluster) = 1;
  end
  
  centers = spdiags(1./cluster_size, 0, num_clusters, num_clusters)*centers;

  
  y = sum(centers.*centers, 2);
  Y = y(:, ones(n, 1));
  P = X + Y - 2*centers*data';

  qnew = sum(sum(sparse(ind, 1:n, 1, size(P, 1), size(P, 2)).*P));

  disp(abs((qnew-qold)/qold));
  if threshold >= abs((qnew-qold)/qold)
  %if iter==timi
    q= qold;
    lables = ind';
    P = sparse(ind, 1:n, 1, num_clusters, n);
    centers = P*data;
    cluster_size = P*ones(n, 1);
    center = spdiags(1./cluster_size, 0, num_clusters, num_clusters)*centers;
    q= qnew;
    nweight;
    break;
  end
  qold = qnew;
   %find 5 center using P
  result=[];
  for i=1:size(P,1)
      max=P(i,1);
      index=1;
      for j=1:size(P,2)
          if(max<P(i,j))
              max=P(i,j);
              index=j;
          end
      end
      result=[result index];
  end
  %disp(result);
  % node attri matrix for five community
 
  one=f(result(1,1),:);
  
  two=f(result(1,2),:);
  
  three=f(result(1,3),:);
  
  four=f(result(1,4),:);
  
  five=f(result(1,5),:); 
  
  six=f(result(1,6),:);
  
  seven=f(result(1,7),:);
  
  for i=1:nn
      if(ind(1,i)==1)
          if(i~=result(1,1))
              one=[one;f(i,:)];
          end
      end
       if(ind(1,i)==2)
          if(i~=result(1,2))
              two=[two;f(i,:)];
          end
       end
       if(ind(1,i)==3)
          if(i~=result(1,3))
              three=[three;f(i,:)];
          end
       end
       if(ind(1,i)==4)
          if(i~=result(1,4))
              four=[four;f(i,:)];
          end
       end
       if(ind(1,i)==5)
          if(i~=result(1,5))
              five=[five;f(i,:)];
          end
       end
       if(ind(1,i)==6)
          if(i~=result(1,6))
              six=[six;f(i,:)];
          end
       end
       if(ind(1,i)==7)
          if(i~=result(1,7))
              seven=[seven;f(i,:)];
          end
      end
  end
  
  % vote using one two three four five matrix
  
   v1=zeros(1,ff); 
   for i=1:ff
       for j=2:size(one,1)
           if(one(1,i)==one(j,i))
               v1(1,i)=v1(1,i)+1;
           end
       end
   end
   v3=zeros(1,ff); 
   for i=1:ff
       for j=2:size(three,1)
           if(three(1,i)==three(j,i))
               v3(1,i)=v3(1,i)+1;
           end
       end
   end
   v2=zeros(1,ff); 
   for i=1:ff
       for j=2:size(two,1)
           if(two(1,i)==two(j,i))
               v2(1,i)=v2(1,i)+1;
           end
       end
   end
   v4=zeros(1,ff); 
   for i=1:ff
       for j=2:size(four,1)
           if(four(1,i)==four(j,i))
               v4(1,i)=v4(1,i)+1;
           end
       end
   end
   v5=zeros(1,ff); 
   for i=1:ff
       for j=2:size(five,1)
           if(five(1,i)==five(j,i))
               v5(1,i)=v5(1,i)+1;
           end
       end
   end
   
    v6=zeros(1,ff); 
   for i=1:ff
       for j=2:size(six,1)
           if(six(1,i)==six(j,i))
               v6(1,i)=v6(1,i)+1;
           end
       end
   end
   
    v7=zeros(1,ff); 
   for i=1:ff
       for j=2:size(seven,1)
           if(seven(1,i)==seven(j,i))
               v7(1,i)=v7(1,i)+1;
           end
       end
   end
   
  tog=[v1;v2;v3;v4;v5;v6;v7];
   
   numerator=sum(tog);
  %[xx,yy]=size(numerator)
  denominator=sum(numerator)/ff;
  % update weight
  delta_weight=numerator./denominator;% 1*104
  nweight=(diag(weight))';
  nweight=(nweight+delta_weight)/2;
  weight=diag(nweight);
  % update data
  data=data';
  data=weight*data;
  data=data'; 
end


function init_centers = random_init(data, num_clusters)
rnd_Idx = randperm(size(data,1),num_clusters);  
init_centers= data(rnd_Idx,:); 