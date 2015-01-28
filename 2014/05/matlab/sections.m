%%% "3d-plot"
[X,Y] = meshgrid(-8:.5:8,-8:.5:8); % Create a mesh grid on [-8,8]*[-8,8].
R = sqrt(X.^2 + Y.^2) + eps; % + eps to avoid divide-by-zero error.
Z = sin(R)./R;
mesh(X,Y,Z)
print -dpng 'mesh.png'

%%% "anon-functions"
cs=4;
myfun = @(x) (x(1)-1).^4+cs*(x(2)-2).^2

%%% "meshgrid-using-anon-fn"
[X,Y] = meshgrid(0:.1:3,0:0.1:6);
tic, for i=1:size(X,1), for j=1:size(X,2), F(i,j)=myfun([X(i,j) Y(i,j)]); end, end, toc
surfc(X,Y,F); xlabel('x_1');ylabel('x_2');zlabel('myfun(x_1,x_2)')
print -dpng 'mesh-with-function.png'

%%% "van-der-pol-def"
xdot=@(t,x) [x(2);(1-x(1)^2)*x(2)-x(1)];

%%% "van-der-pol-solve"
[t,x_t]=ode45(xdot,[0 20],[2 0]);

%%% "van-der-pol-plot"
plot(t,x_t);grid;xlabel('time');ylabel('x');
title('Van der Pol Equation');legend('x_1','x_2');
print -dpng 'van-der-pol.png';

%%% "van-der-pol-simulink"
open('vdp');
set_param('vdp/Scope','LimitDataPoints','off','SaveToWorkspace','on');
sim('vdp');
plot(ScopeData(:,1),ScopeData(:,[2 3]));grid;xlabel('Time (s)');ylabel('x');title('Van der Pol Simulation');
print -dpng 'van-der-pol-simulink.png';

%%% "print-simulink-model"
print -dpng -svdp 'van-der-pol-simulink-model.png'

%%% "close"
close_system('vdp',0);

%%% "write-js"
addpath('jsonlab')
foo = 5; bar = 7;
vars = struct('foo', foo, 'bar', bar, 'pi', pi)
fid = fopen('values.json', 'w');
fprintf(fid, '%s', savejson(vars));
fclose(fid);

%%% "help"
help publish
