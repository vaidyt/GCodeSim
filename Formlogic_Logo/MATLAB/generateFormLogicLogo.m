function generateFormLogicLogo

clear;
clc;
close all;

load('Formlogic_Logo.mat');

nRows = size(boolGrid,1);
nCols = size(boolGrid,2);

lineSegments = [];

cellCount = 1;

for i = 1 : nRows
    thisRow = boolGrid(i,:);
    % identify all the connected components in this horizontal line
    CC = bwconncomp( thisRow );
    nConnectedComponents = length(CC.PixelIdxList);
    % Loop over all the connected components and identify its extents
    for j = 1 : nConnectedComponents
        thisPixelId = CC.PixelIdxList{j};
        lineSegments{cellCount} = [min(thisPixelId) i max(thisPixelId) i] - 1;
        cellCount = cellCount + 1;
    end
end

globalGcode = [];
for i = 1 : length(lineSegments)
    % Generate the g-code for this horizontal line segment
    thisGcode = getGCodeForLine(lineSegments{i});
    % append it to the whole g-code
    globalGcode = [globalGcode; thisGcode];
end

% write the whole g-code cell array to a file
filePh = fopen('FormLogic.gcode','w');
fprintf(filePh,'%s\n',globalGcode{:});
fclose(filePh);
disp('Done creating gcode');

end

% Generates the g-code for a given line segment
function gcode = getGCodeForLine( lineSegment )
    gcode = cell(4,1);
    
    % Go
    gcode{1} = sprintf('G01 X%d Y%d', lineSegment(1), lineSegment(2));
    % Laser on
    gcode{2} = 'M01';
    % Go
    gcode{3} = sprintf('G01 X%d Y%d', lineSegment(3), lineSegment(4));
    % Laser off
    gcode{4} = 'M01';
end
