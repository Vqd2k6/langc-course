**"Four Chunking Variables that affect quality"** (4 biến số khi chia nhỏ văn bản quyết định trực tiếp đến chất lượng của hệ thống RAG). Hãy cùng bóc tách 4 góc phần tư trên slide:

---

### 1. CHUNK SIZE (Kích thước đoạn cắt - Góc trên bên trái)

Biến số này quy định mỗi đoạn văn bản được cắt ra chứa bao nhiêu token hoặc ký tự.

* **Too Small (Quá nhỏ):**
* *Hệ quả:* **Loses context** (Mất ngữ cảnh).
* Ví dụ nếu cắt từng câu hoặc cụm vài chục từ, đoạn cắt sẽ không đủ ý nghĩa trọn vẹn, vector embedding sinh ra bị rời rạc, LLM khi nhận đoạn này sẽ không hiểu được bối cảnh xung quanh.


* **Too Large (Quá lớn):**
* *Hệ quả:* **Dilutes meaning** (Làm loãng ý nghĩa).
* Giống như quả bóng bị thổi quá to, một đoạn văn bản hàng nghìn từ chứa quá nhiều chủ đề hỗn tạp sẽ làm vector embedding bị mờ nhạt, giảm độ chính xác khi so khớp độ tương đồng ngữ nghĩa.


* **Sweet spot (Điểm cân bằng lý tưởng):**
* Khoảng **200 – 1000 tokens**. Đây là kích thước thực nghiệm tối ưu cho hầu hết các mô hình Embedding hiện đại, vừa bảo toàn một luận điểm trọn vẹn, vừa giúp biểu diễn vector sắc nét.



---

### 2. OVERLAP (Độ chồng lấn - Góc trên bên phải)

Khi cắt tài liệu thành các khối liên tiếp (`Chunk 1`, `Chunk 2`), phần **Overlap** (vùng gạch chéo màu cam) chính là đoạn văn bản bị lặp lại ở cuối Chunk 1 và đầu Chunk 2.

* **Tỷ lệ khuyến nghị:** **10 - 20% overlap**.
* **Mục đích:** **Preserves context** (Bảo toàn ngữ cảnh tại ranh giới cắt).
* **Tại sao cần Overlap?** Nếu một câu quan trọng hoặc một định nghĩa bị chiếc kéo thuật toán cắt đôi làm hai nửa (nửa nằm ở Chunk 1, nửa trôi sang Chunk 2), thông tin đó sẽ bị phá hủy. Độ gối đầu 10-20% đảm bảo không có mối nối hay thông tin bản lề nào bị đứt gãy.

---

### 3. SPLIT BOUNDARIES (Ranh giới cắt đoạn - Góc dưới bên trái)

Đây là chiến lược quyết định *nơi chiếc kéo sẽ hạ xuống* để chia tách văn bản:

* **Fixed (Cắt cố định):**
* Cắt cơ học đúng số lượng ký tự/token (ví dụ: cứ đủ 500 ký tự là cắt).
* *Hạn chế:* Rất dễ cắt ngang giữa một từ hoặc giữa một câu (`random cut`).


* **Recursive (Đệ quy):**
* Chiến lược phổ biến nhất trong LangChain (`RecursiveCharacterTextSplitter`).
* Thuật toán sẽ ưu tiên cắt ở các ranh giới tự nhiên theo thứ tự ưu tiên: Đoạn văn (`\n\n`) $\rightarrow$ Dòng đơn (`\n`) $\rightarrow$ Dấu chấm câu/khoảng trắng (`cutting at paragraphs/sentences`).


* **Semantic (Ngữ nghĩa - Có viền xanh phát sáng / Đánh giá là `best`):**
* `cutting at meaning boundaries`: Không dựa vào độ dài ký tự thô mà dùng chính mô hình embedding để đo khoảng cách ngữ nghĩa giữa các câu liên tiếp. Khi nào phát hiện có sự chuyển đổi chủ đề (semantic drift), thuật toán mới thực hiện cắt đoạn.



---

### 4. CONTENT TYPE (Đặc thù loại nội dung - Góc dưới bên phải)

Thông điệp cốt lõi ở góc này là: **"Each needs different treatment"** (Mỗi loại dữ liệu đòi hỏi một phương pháp cắt khác nhau, không thể dùng chung một công thức):

* **Code (`{...}`):** Mã nguồn cần được cắt theo cấu trúc ngôn ngữ (theo hàm `def`, class, block code). Nếu cắt ngang thân một vòng lặp `for`, đoạn code sẽ mất cấu trúc cú pháp. LangChain cung cấp sẵn `Language.PYTHON`, `Language.JS`,...
* **Legal (Tài liệu pháp lý / Hợp đồng):** Văn bản luật có cấu trúc Điều, Khoản, Điểm rất chặt chẽ. Cắt tài liệu luật phải tôn trọng cấu trúc cây điều khoản thay vì cắt theo số lượng token.
* **Markdown (`#`):** Văn bản phân cấp theo tiêu đề H1, H2, H3. Nên dùng `MarkdownHeaderTextSplitter` để tách theo từng đề mục nhằm đính kèm luôn tên thẻ Header vào metadata của từng chunk.

---

### Tóm tắt góc nhìn Production

Khi tinh chỉnh Pipeline RAG trong thực tế:

1. Luôn bắt đầu thử nghiệm với **Recursive Splitter** ở mức `chunk_size = 500 - 800 tokens` và `chunk_overlap = 100 - 150 tokens`.
2. Định dạng nội dung là gì thì dùng Splitter chuyên biệt của định dạng đó (Markdown, HTML, Code) trước khi đưa vào embedding.