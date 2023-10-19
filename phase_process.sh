green=`tput setaf 2`
reset=`tput sgr0`
# File DIR
DATASET=movies
LOWER_CASE_DIR=./data
LOWER_CASE_FILE=${DATASET}_combined_lower_case.txt
INPUT_FILE=${DATASET}_combined.txt
DIR=./data/${DATASET}_autophrase
SEGMENTATION_FILE=segmentation_${DATASET}_lower_case.txt
# Add lower case segmentation
if [ ! -f "${LOWER_CASE_DIR}/$LOWER_CASE_FILE" ]; then
	echo "Converting to Lowecase"
	python utils.py --mode 0  --dataset ${LOWER_CASE_DIR} --in_file ${INPUT_FILE} --out_file ${LOWER_CASE_DIR}/${LOWER_CASE_FILE}
fi


# Segmented file

echo ${green}===Phrase Processing===${reset}
python utils.py --dataset ${DIR} --in_file ${SEGMENTATION_FILE} --out_file ${DIR}/phrase_text.txt
