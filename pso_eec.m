clear all
xm=200;
ym=200;
sink.x=100;  %location of sink on x-axis
sink.y=100;  %location of sink on y-axis
n=70;  %nodes
D=floor(0.07*n);
m=D;  %number of CH
%P=0.1;  %probability of cluster heads
Eo=2; %initial energy
ETX=50*0.000000001;  %tx energy
ERX=50*0.000000001;  %rx energy
Efs=10*0.000000000001;  %free space loss
Emp=0.0013*0.000000000001;   %multi path loss
dmax=100;
S(n+1).xd=sink.x; %sink is a n+1 node, x-axis postion of a node
S(n+1).yd=sink.y; %sink is a n+1 node, y-axis postion of a node
S(n+1).E=Inf;
%Data Aggregation Energy
EDA=5*0.000000001;  %compression energy
a=1;   %fraction of energy enhancment of advance nodes
rmax=2000;  %maximum number of rounds
do=sqrt(Efs/Emp);  %distance do is measured
Et=0;  %variable just use below 
A=0;
itt=1;
for i=1:1:n
    S(i).xd=rand(1,1)*xm;  %generates a random no. use to randomly distibutes nodes on x axis
    XR(i)=S(i).xd;
    S(i).yd=rand(1,1)*ym;  %generates a random no. use to randomly distibutes nodes on y axis
    YR(i)=S(i).yd;
    S(i).G=0; %node is elegible to become cluster head
    S(i).E=Eo;
    E(i)= S(i).E;
    Et=Et+E(i);  %estimating total energy of the network
    %initially there are no cluster heads only nodes
    if (mod(i,14)==0)
    S(i).type='C';
    C(itt).xd=S(i).xd;
    C(itt).yd=S(i).yd;
    distance=sqrt( (S(i).xd-(S(n+1).xd) )^2 + (S(i).yd-(S(n+1).yd) )^2 );
    C(itt).distance=distance;
    C(itt).id=i;
    arr(itt).sum=0;
    arr(itt).number=0;
    itt=itt+1;
    else
     S(i).type='N';
    end
     arr(itt).sum=0;
     arr(itt).number=0;
end
f2=1/(Eo*m);


for i=1:1:n
   if ( S(i).type=='N' && S(i).E>0 )
     if(m-1>=1)
       min_dis=sqrt( (S(i).xd-S(n+1).xd)^2 + (S(i).yd-S(n+1).yd)^2 );
       min_dis_cluster=m+1;
       for c=1:1:m
           temp=min(min_dis,sqrt( (S(i).xd-C(c).xd)^2 + (S(i).yd-C(c).yd)^2 ) );
           if ( temp<min_dis )
               min_dis=temp;
               min_dis_cluster=c;
           end
       end
       arr(round(min_dis_cluster)).sum=arr(round(min_dis_cluster)).sum+min_dis;
       arr(round(min_dis_cluster)).number=arr(round(min_dis_cluster)).number+1;
     end
   end
end
f1=0;
for i=1:1:m
       distance=sqrt( (C(i).xd-(S(n+1).xd) )^2 + (C(i).yd-(S(n+1).yd) )^2 );
     f1=f1+((distance)+arr(i).sum)/arr(i).number;  
end
f1=f1/1000;


for i=1:1:n
    alpha=0.3;
    S(i).pbest=alpha*f1+(1-alpha)*f2;
end

gbest=S(1).pbest;
for i=2:1:n
    if(gbest>S(i).pbest)
        gbest=S(i).pbest;
    end
    S(i).xvel=0;
    S(i).yvel=0;
    
end
flag_first_dead=0; %flag tells the first node dead
flag_teenth_dead=0;  %flag tells the 10th node dead
flag_all_dead=0;  %flag tells all nodes dead
dead=0;  %dead nodes count initialized to 0
first_dead=0;
teenth_dead=0;
all_dead=0;
allive=n;

for j=1:1:rmax
  j
   %B = nestedSortStruct(S, 'pbest');
    
    for i=1:1:n
            if(S(i).type=='C')
                plot(S(i).xd,S(i).yd,'ko');
                hold on;
            elseif(S(i).type=='N')
                plot(S(i).xd,S(i).yd,'rx');
                hold on;
            end
    end
    
  
    Etotal=0;
    for i=2:1:n
        Etotal=Etotal+S(i).E;
    end
    stat.totalenergy(j+1)=Etotal;
    stat.avgenergy(j+1)=Etotal/n;
    dead=0;
for i=1:1:n
   
    if (S(i).E<=0)
        dead=dead+1; 
        if (dead==1)
           if(flag_first_dead==0)
              first_dead=j;
              flag_first_dead=1;
           end
        end
        if(dead==0.1*n)
           if(flag_teenth_dead==0)
              teenth_dead=j;
              flag_teenth_dead=1;
           end
        end
        if(dead==n)
           if(flag_all_dead==0)
              all_dead=j;
              flag_all_dead=1;
           end
        end
    end
    if S(i).E>0
        S(i).type='N';
    end
end
STATISTICS.DEAD(j+1)=dead;
STATISTICS.ALLIVE(j+1)=allive-dead;
    
    for k=1:1:n
        w=rand()*1;
        c1=(rand*1)+(rand*1);
        c2=(rand*1)+(rand*1);
        x1=(rand*1);
        x2=(rand*1);
        
        S(k).xvel=w*S(k).xvel+(c1*x1*(S(k).pbest-S(k).xd))+(c2*x2*(gbest-S(k).xd));
        S(k).yvel=w*S(k).yvel+(c1*x1*(S(k).pbest-S(k).yd))+(c2*x2*(gbest-S(k).yd));
        S(k).xd=S(k).xd+S(k).xvel;
        S(k).yd=S(k).yd+S(k).yvel;
        if(S(k).xd<0)
            S(k).xd=0;
        end
        if(S(k).yd<0)
            S(k).yd=0;
        end
        if(S(k).xd>200)
            S(k).xd=200;
        end
        if(S(k).yd>200)
            S(k).yd=200;
        end
            
       
                         for i=1:1:n
                           if ((S(i).E>0) )
                               if(S(i).type=='N')
                                 if(m-1>=1)
                                   min_dis=sqrt( (S(i).xd-S(n+1).xd)^2 + (S(i).yd-S(n+1).yd)^2 );
                                   min_dis_cluster=m+1;
                                   for c=1:1:m
                                       temp=min(min_dis,sqrt( (S(i).xd-C(c).xd)^2 + (S(i).yd-C(c).yd)^2 ) );
                                       if ( temp<min_dis )
                                           min_dis=temp;
                                           min_dis_cluster=c;
                                       end
                                   end
                                   arr(round(min_dis_cluster)).sum=arr(round(min_dis_cluster)).sum+min_dis;
                                   arr(round(min_dis_cluster)).number=arr(round(min_dis_cluster)).number+1;
                                 end
                               end
                           end
                           if(S(i).E<=0)
                           S(i).E=0;
                           end
                         end
                        f1=0;
                        ECHtotal=0;
                        for i=1:1:m
                             distance=sqrt( (C(i).xd-(S(n+1).xd) )^2 + (C(i).yd-(S(n+1).yd) )^2 );
                             f1=f1+((distance)+arr(i).sum)/arr(i).number;
                             ECHtotal=ECHtotal+S(C(i).id).E;
                        end
                        f1=f1/1000;
                        f2=1/ECHtotal;

                        alpha=0.3;
                            fitness=alpha*f1+(1-alpha)*f2;
                            if(fitness<S(k).pbest)
                            S(k).pbest=fitness;
                            end
                        ar(k)=S(k).pbest;

                        gbest=S(1).pbest;
                        for i=2:1:n
                            if(gbest>S(i).pbest)
                                gbest=S(i).pbest;
                            end
                        end
                            if(fitness<gbest)
                            gbest=fitness;
                            end
    end         
          
    
    
     for i=1:1:n
                           if ((S(i).E>0) )
                               if(S(i).type=='N')
                                   min_dis=sqrt( (S(i).xd-S(n+1).xd)^2 + (S(i).yd-S(n+1).yd)^2 );
                                   min_dis_cluster=m;
                                   for c=1:1:m
                                       temp=min(min_dis,sqrt( (S(i).xd-S(C(c).id).xd)^2 + (S(i).yd-S(C(c).id).yd)^2 ) );
                                       if ( temp<min_dis )
                                           min_dis=temp;
                                           min_dis_cluster=c;
                                       end
                                   end
                                   
                                   if (min_dis>do)
                                        S(i).E=S(i).E- ( ETX*(4000) + Emp*4000*( min_dis * min_dis * min_dis * min_dis)); 
                                    end
                                    if (min_dis<=do)
                                        S(i).E=S(i).E- ( ETX*(4000) + Efs*4000*( min_dis * min_dis)); 
                                    end

                                    S(C(min_dis_cluster).id).E = S(C(min_dis_cluster).id).E- ( (ERX + EDA)*4000 ); 
                                   
                               end
                                 if(S(i).type=='C')
                                     min_dis=sqrt( (S(i).xd-(S(n+1).xd) )^2 + (S(i).yd-(S(n+1).yd) )^2 );
                                    if (min_dis>do)
                                        S(i).E=S(i).E- ( ETX*(4000) + Emp*4000*( min_dis * min_dis * min_dis * min_dis)); 
                                    end
                                    if (min_dis<=do)
                                        S(i).E=S(i).E- ( ETX*(4000) + Efs*4000*( min_dis * min_dis)); 
                                    end
                                 end
                           end
                           
                           if(S(i).E<=0)
                           S(i).E=0;
                           end
     end
    
      for i=1:1:n
      ar(i)=S(i).pbest;
      end
          so=sort(ar);
        base_value=so(m);
   
    count2=0;
           for countt=1:1:n
              S(i).type='N';
               if(S(countt).pbest<base_value)
                  count2=count2+1;
                   S(countt).type='C';
                   C(count2).id=countt;
               end
           
           end 
    
end
first_dead
teenth_dead
all_dead

figure,plot(STATISTICS.DEAD),title('TOTAL DEAD NODES'),xlabel({'no of rounds'}),ylabel({'total no. of dead nodes'});
figure,plot(STATISTICS.ALLIVE),title('TOTAL ALIVE NODES'),xlabel({'no of rounds'}),ylabel({'total no. of alive nodes'});
figure,plot(stat.totalenergy),title('TOTAL ENERGY'),xlabel({'no of rounds'}),ylabel({'total energy'});
figure,plot(stat.avgenergy),title('AVERAGE ENERGY'),xlabel({'no of rounds'}),ylabel({'average energy'});




